from ipaddress import ip_address
import logging
from time import sleep
from urllib.parse import quote
from proxmoxer import ProxmoxAPI
from ezinfra.sshkeys import get_ssh_pubkey_from_privatekey, get_privatekey_from_string
from ezinfra.remote import wait_for_ssh
from ezlab.parameters import SWAP_DISK_SIZE, TASK_FINISHED
from ezlab.utils import ezapp

logger = logging.getLogger()

def connect(host, username, password):
    result = None
    try:
        result = ProxmoxAPI(
            host,
            user=username,
            password=password,
            verify_ssl=False,
        )
    except Exception as error:
        return error

    return result


def vms(proxmox):
    return proxmox.cluster.resources.get(type="vm")


def storage(proxmox):
    return proxmox.cluster.resources.get(type="storage")


def networks(proxmox):
    return proxmox.cluster.resources.get(type="sdn")


def bridges(proxmox, fromtemplatename):
    if not fromtemplatename or fromtemplatename == "":
        return []

    try:
        template = [
            t for t in vms(proxmox) if t["template"] and t["name"] == fromtemplatename
        ].pop()
    except IndexError:
        return []

    return (
        proxmox.nodes(template["node"]).network.get(type="any_bridge")
        if template
        else []
    )


def clone(
    resources: tuple,
    settings: dict,
    vm_number: int,
    dryrun: bool,
):
    template, volume, bridge, eznode, hostname, first_ip = resources

    node = template["node"]
    template_type = template["type"]
    template_id = template["vmid"]

    vm_gateway = settings["gateway"]
    vm_network_bits = settings["cidr"].split("/")[1]
    privatekey: str = settings["privatekey"]

    # cloudinit requires OpenSSH format public key
    pk = get_privatekey_from_string(privatekey)
    publickey = get_ssh_pubkey_from_privatekey(pk)

    multivm = vm_number > 0 
    vm_name = hostname + str(vm_number if multivm else "")

    ezapp.queue.put(f"[ {vm_name} ] cloning...")
    # wait for others to request vmid
    sleep(vm_number * 4)
    nextid = ezapp.connection.cluster.nextid.get()
    ezapp.queue.put(f"[ {vm_name} ] assigned id {nextid}")

    ipconfig = "ip="
    vm_ip = ""
    if first_ip == "dhcp":
        ipconfig += "dhcp"
    else:
        vm_ip = str(
            ip_address(first_ip) + vm_number - 1 if multivm else ip_address(first_ip)
        )  # adjust for single VM
        ipconfig += f"{vm_ip}/{vm_network_bits}"
        ipconfig += f",gw={vm_gateway}"

    ezapp.queue.put(f"[ {vm_name} ] ({nextid}) creating")

    if dryrun:
       ezapp.queue.put(f"Would clone VM as {vm_name}")

    else:
        try:
            result = task_waitfor(
                ezapp.connection,
                node,
                ezapp.connection.nodes(node)(template_type)(template_id).clone.post(
                    newid=nextid,
                    name=vm_name,
                    description=eznode["name"],
                ),
            )
            if result == TASK_FINISHED:
                new_vm = ezapp.connection.nodes(node)(template_type)(nextid)
                ezapp.queue.put(f"[ {vm_name} ] cloned")
            else:
                ezapp.queue.put(f"PVE CLONE FAILED for {vm_name}: {result}")
                ezapp.queue.put(TASK_FINISHED)
                return False
        except Exception as error:
            ezapp.queue.put(f"PVE VMCLONE EXCEPTION for {vm_name}: {error}")
            ezapp.queue.put(TASK_FINISHED)
            return False

    if dryrun:
        ezapp.queue.put(f"""Would update VM config with:
            cores={eznode["cores"]},
            memory={eznode["memGB"] * 1024},
            net0={f"virtio,bridge={bridge},firewall=0"},
            ipconfig0={ipconfig},
            tags={eznode["product"]},
            ciuser={settings["username"]},
            cipassword={'*'*8},
            nameserver={settings["nameserver"]},
            searchdomain={settings["domain"]},
            ciupgrade=0,
            sshkeys={quote(publickey, safe="")},
            onboot=1,
            efidisk0={volume['storage']}:1,efitype=4m,pre-enrolled-keys=1,size=4M",
                  """)

    else:
        # configure vm
        ezapp.queue.put(f"[ {vm_name} ] reconfigure")
        try:
            new_vm.config.post(
                cores=eznode["cores"],
                memory=eznode["memGB"] * 1024,
                net0=f"virtio,bridge={bridge},firewall=0",
                ipconfig0=ipconfig,
                tags=eznode["product"],
                ciuser=settings["username"],
                cipassword=settings["password"],
                nameserver=settings["nameserver"],
                searchdomain=settings["domain"],
                ciupgrade=0,
                sshkeys=quote(publickey, safe=""),
                onboot=1,
                efidisk0=f"{volume['storage']}:1,efitype=4m,pre-enrolled-keys=1,size=4M",
            )
            ezapp.queue.put(f"[ {vm_name} ] reconfigured")
        except Exception as error:
            ezapp.queue.put(f"PVE VMCONFIG EXCEPTION for {vm_name}: {error}")
            ezapp.queue.put(TASK_FINISHED)
            return False

    if dryrun:
        ezapp.queue.put(
            f"""Would configure disks:
                  OS Disk: {eznode['os_disk_size']}G
                  Swap Disk: {SWAP_DISK_SIZE}G
                  Data Disks (qty: {eznode["no_of_disks"]}): {volume['storage']}:{eznode['data_disk_size']},backup=0,discard=on,cache=unsafe,iothread=1,replicate=0,ssd=1
                  """
        )

    else:
        ezapp.queue.put(f"[ {vm_name} ] add disks")
        try:
            # configure disks
            new_vm.resize.put(disk="scsi0", size=f"{eznode['os_disk_size']}G")
            # create swap disk (recommended for DF 10% of memGB) with roundup
            # Use fixed size for swap, so installer script can find it
            # swap_size = int(eznode["memGB"] // 10 + 1)
            swap_disk = f"{volume['storage']}:{SWAP_DISK_SIZE},backup=0,discard=on,cache=unsafe,iothread=1,replicate=0,ssd=1"
            new_vm.config.post(scsi1=swap_disk)

            ezapp.queue.put(f"[ {vm_name} ] {SWAP_DISK_SIZE}GB swap disk added")
            # add data disks /// assume no_of_disks are 0 or 1 or 2
            data_disk = f"{volume['storage']}:{eznode['data_disk_size'] if 'data_disk_size' in eznode else 0},backup=0,discard=on,cache=unsafe,iothread=1,replicate=0,ssd=1"
            if eznode["no_of_disks"] > 0:
                new_vm.config.post(scsi2=data_disk)
            if eznode["no_of_disks"] > 1:
                new_vm.config.post(scsi2=data_disk, scsi3=data_disk)

            ezapp.queue.put(f"[ {vm_name} ] disks attached")
        except Exception as error:
            ezapp.queue.put(f"PVE VMUPDATE EXCEPTION for {vm_name}: {error}")
            ezapp.queue.put(TASK_FINISHED)
            return False

        # start vm
        new_vm.status.start.post()

        ezapp.queue.put(f"[ {vm_name} ] waiting startup...")

        # # apply customisations to vm

        if not wait_for_ssh(vm_ip, settings["username"], settings["privatekey"]):
            ezapp.queue.put(f"[{vm_ip}] SSH FAILED")
            ezapp.queue.put(TASK_FINISHED)
            return False

        # # reboot for changes
        # task_waitfor(
        #     connection=proxmox,
        #     node=node,
        #     task_id=new_vm.status.reboot.post(timeout=60),
        #     title=f"reboot {vm_name}",
        # )
        ezapp.queue.put(f"[ {vm_name} ] ready for {eznode['product']}")
        ezapp.queue.put(TASK_FINISHED)
        return True

    # catch all
    ezapp.queue.put(TASK_FINISHED)
    return True


def task_waitfor(proxmox, node, task_id):
    task_submitted = proxmox.nodes(node).tasks(task_id).status.get()
    if task_submitted["status"] == "stopped":
        return task_submitted["exitstatus"]

    try:
        status = proxmox.nodes(node).tasks(task_id).status.get()
        while status["status"] != "stopped":
            print(f"PVE TASK: {status['type']} is {status['status']}")
            sleep(3)
            status = proxmox.nodes(node).tasks(task_id).status.get()
    except Exception as error:
        return error

    return TASK_FINISHED

import os

from ezlab.parameters import DF, GENERIC, UA

ini_file = os.path.expanduser("~/.ezconfig.ini")

# class ez_product(str, Enum):
#     df = "ezdf"
#     ua = "ezua"
#     generic = "generic"

# ez_nodes = [
#     {
#         "name": "ua-control",
#         "product": UA,
#         "cores": 4,
#         "memGB": 8,
#         "os_disk_size": 300,
#         "data_disk_size": 500,
#         "no_of_disks": 1,
#         "count": 2,
#     },
#     {
#         "name": "ua-worker",
#         "product": UA,
#         "cores": 32,
#         "memGB": 128,
#         "os_disk_size": 300,
#         "data_disk_size": 500,
#         "no_of_disks": 2,
#         "count": 3,
#     },
#     {
#         "name": "df-singlenode",
#         "product": DF,
#         "cores": 32,
#         "memGB": 96,
#         "os_disk_size": 200,
#         "data_disk_size": 500,
#         "no_of_disks": 1,
#         "count": 1,
#     },
#     {
#         "name": "df-5nodes",
#         "product": DF,
#         "cores": 16,
#         "memGB": 34,
#         "os_disk_size": 200,
#         "data_disk_size": 500,
#         "no_of_disks": 1,
#         "count": 5,
#     },
#     {
#         "name": "client",
#         "product": GENERIC,
#         "cores": 2,
#         "memGB": 4,
#         "os_disk_size": 50,
#         "no_of_disks": 0,
#         "count": 1,
#     },
#     {
#         "name": "generic",
#         "product": GENERIC,
#         "cores": 1,
#         "memGB": 2,
#         "os_disk_size": 20,
#         "no_of_disks": 0,
#         "count": 1,
#     },
# ]


ez_files = {
    DF: {
        "/etc/sysctl.d/mapr.conf": "vm.swappiness=1\n",
        "/etc/profile.d/mapr.sh": "umask 0022\n",
    },
    UA: {},
    GENERIC: {},
}

# ez_commands = {
#     DF: [
#         # "sudo chown root:root /etc/sudoers.d/mapr -- 2>/dev/null && sudo chmod 440 /etc/sudoers.d/mapr",
#         # disable subscription manager - TODO: needs testing
#         "[ -f /etc/yum/pluginconf.d/product-id.conf ] && sudo sed -i 's/^enabled=0/enabled=1/' /etc/yum/pluginconf.d/product-id.conf",
#         "[ -f /etc/yum/pluginconf.d/subscription-manager.conf ] && sudo sed -i 's/^enabled=0/enabled=1/' /etc/yum/pluginconf.d/subscription-manager.conf",
#         "sudo sysctl vm.swappiness=1 > /dev/null",
#         # "sudo systemctl disable --now numad",
#         "sudo sed -i 's/^[^#]*PasswordAuthentication[[:space:]]no/PasswordAuthentication yes/' /etc/ssh/sshd_config",
#         "sudo systemctl restart sshd",
#         "sudo dnf install -y -q wget > /dev/null",
#     ],
#     UA: [
#         # disable subscription manager - TODO: needs testing
#         "[ -f /etc/yum/pluginconf.d/product-id.conf ] && sudo sed -i 's/^enabled=0/enabled=1/' /etc/yum/pluginconf.d/product-id.conf",
#         "[ -f /etc/yum/pluginconf.d/subscription-manager.conf ] && sudo sed -i 's/^enabled=0/enabled=1/' /etc/yum/pluginconf.d/subscription-manager.conf",
#         "sudo dnf -q -y install nfs-utils policycoreutils-python-utils conntrack-tools jq tar >/dev/null",
#         "sudo dnf --setopt=tsflags=noscripts install -y -q iscsi-initiator-utils >/dev/null",
#         'echo "InitiatorName=$(/sbin/iscsi-iname)" | sudo tee -a /etc/iscsi/initiatorname.iscsi >/dev/null',
#         "sudo systemctl enable --now iscsid 2>&1 > /dev/null",
#         "sudo ethtool -K eth0 tx-checksum-ip-generic off >/dev/null",
#         "sudo sed -i 's/^[^#]*PermitRootLogin[[:space:]]no/PermitRootLogin yes/' /etc/ssh/sshd_config",
#         "sudo systemctl restart sshd",
#     ],
#     GENERIC: [
#         "[ -f /etc/yum/pluginconf.d/product-id.conf ] && sudo sed -i 's/^enabled=0/enabled=1/' /etc/yum/pluginconf.d/product-id.conf",
#         "[ -f /etc/yum/pluginconf.d/subscription-manager.conf ] && sudo sed -i 's/^enabled=0/enabled=1/' /etc/yum/pluginconf.d/subscription-manager.conf",
#         "sudo sed -i 's/^[^#]*PasswordAuthentication[[:space:]]no/PasswordAuthentication yes/' /etc/ssh/sshd_config",
#         "sudo systemctl restart sshd",
#     ],
# }

ez_installers = {
    DF: {
        "image": "maprtech/edf-seed-container:latest",
        "start_installer": "./datafabric_container_setup.sh",
        "url": "https://localhost:8443/app/dfui/#/installer",
        "commands": [],
    },
    UA: {
        "start_installer": "./start_ezua_installer_ui.sh",
        # "image": "marketplace.us1.greenlake-hpe.com/ezua/ezua/hpe-ezua-installer-ui:latest",
        "image": "us.gcr.io/mapr-252711/hpe-ezua-installer-ui:1.2.0-d16afb0",
        "url": "http://localhost:8080",
    },
    GENERIC: {},
}

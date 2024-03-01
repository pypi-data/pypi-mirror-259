from datetime import datetime
import logging
import importlib_resources
from nicegui import app, ui, run, native
import inspect

import requests

from ezshow import apprunner
from ezshow import shrunner
from ezshow import restrunner
import ezshow
from ezlab.utils import DEMOS
from ezshow.elements import get_echart, monitor_chart

logger = logging.getLogger("ezshow")
# Disable annoying messages in log view
# Thanks to: https://sam.hooke.me/note/2023/10/nicegui-binding-propagation-warning/
import nicegui.binding


# Increase threshold for binding propagation warning from 0.01 to 0.02 seconds
nicegui.binding.MAX_PROPAGATION_TIME = 0.03

if not DEMOS:
    print("Failed to load demos!")
    exit(1)


@ui.page("/")
def menu():
    # initialize app storage for demos
    if "ui" not in app.storage.general.keys():
        app.storage.general["ui"] = {}
    if "demo" not in app.storage.general.keys():
        app.storage.general["demo"] = {}

    appstore = app.storage.general["demo"]

    app.storage.user["busy"] = False

    with (
        ui.expansion(
            "Demos",
            icon="apps",
            caption="guided demos",
        )
        .classes("w-full")
        .classes("text-bold") as ezshow_menu
    ):
        # Connect to a cluster
        ui.label("Use cluster")
        with ui.row().classes("w-full"):
            # ui.input("Cluster Name", placeholder="edf-core").bind_value(
            #     appstore, "clustername"
            # )
            ui.input("Host", placeholder="node1.cluster.lab").bind_value(
                appstore, "host"
            )
            ui.input("Username", placeholder="mapr").bind_value(appstore, "username")
            ui.input(
                "Password",
                placeholder="mapr",
                password=True,
                password_toggle_button=True,
            ).bind_value(appstore, "password")
            # ui.button(
            #     "Login",
            #     on_click=login,
            # ).bind_enabled_from(
            #     app.storage.user, "busy", backward=lambda x: not x
            # ).bind_visibility_from(app.storage.user, "cookiejar", lambda x: x is None)

        demo_tabs = {}
        # Demos (Tabs)
        with ui.tabs().classes("w-full") as tabs:
            for demo in DEMOS:
                demo_tabs[demo["name"]] = ui.tab(demo["name"])

        # Demo content
        with (
            ui.tab_panels(tabs)
            .classes("w-full")
            .bind_value(app.storage.general["demo"], "name")
        ):
            for demo in DEMOS:

                # Demo panel
                with ui.tab_panel(demo_tabs[demo["name"]]):
                    ui.markdown(demo["description"]).classes("font-normal")
                    ui.separator()
                    ui.image(
                        importlib_resources.files("ezshow.demos").joinpath(
                            f"{demo['diagram']}"
                        )
                    ).classes("object-scale-down g-10")

                    ui.link(
                        "Source",
                        target=demo.get("link", "https://github.com/mapr-demos/"),
                        new_tab=True,
                    ).bind_visibility_from(
                        demo, "link", backward=lambda x: x is not None
                    )
                    ui.separator()
                    ui.label("Follow the steps...")
                    with ui.row():
                        ui.label("Using volume:")
                        ui.label(demo.get("volume", "/"))

                    # Steps
                    with (
                        ui.stepper()
                        .props("vertical header-nav")
                        .classes("w-full") as stepper
                    ):
                        for step in demo["steps"]:

                            # Step #
                            with ui.step(step["id"], title=step["name"].title()).props(
                                f"active-icon=play_arrow caption=\"using {step['runner']}\""
                            ):
                                ui.markdown(step["description"]).classes("font-normal")
                                if step["runner"] == "rest":
                                    ui.label(
                                        f"https://{appstore['host']}:8443{step['runner_target']}"
                                    )

                                elif step['runner'] in ['app', 'noop']:
                                    # Display source code if 'codes' provided
                                    if 'codes' in step.keys():
                                        for c in step['codes']:
                                            t = c.split('.')
                                            module_name=getattr(ezshow, t[0])
                                            function_name=t[1]

                                            ui.code(
                                                inspect.getsource(
                                                    getattr(
                                                        module_name,
                                                        function_name
                                                    )
                                                )
                                            ).classes("w-full")
                                            ui.separator()
                                    else:
                                        ui.label(step["runner_target"])
                                    if step['runner'] != "noop":
                                        # Display function params if 'count' is provided
                                        if 'count' in step.keys():
                                            ui.label().bind_text_from(
                                                app.storage.user,
                                                f"count__{demo['name'].replace(' ', '_')}__{step['id']}",
                                                # format message to show function(param, count) format
                                                backward=lambda x, y=step.get(
                                                    "runner_parameters", None
                                                ), p=step["runner_target"]: f"Will be running: {p}( {y}, {x} )"
                                            )
                                        else:
                                            ui.label(f"Will be running: {step['runner_target']} ( {step.get('runner_parameters', None)} )" )

                                # Insert count slider if step wants one
                                if step.get("count", None):
                                    with ui.row().classes("w-full"):
                                        slider = ui.slider(
                                            min=0,
                                            max=3*step['count'],
                                            step=1,
                                            value=step["count"],
                                            # saving selection in user storage, with demo name (spaces substituted with _), step id and parameter
                                        ).bind_value_to(
                                            app.storage.user,
                                            f"count__{demo['name'].replace(' ', '_')}__{step['id']}",
                                        ).classes("w-5/6 self-center")
                                        ui.label().bind_text_from(
                                            slider, "value"
                                        ).classes("self-center")

                                # Get input if step wants one
                                if step.get("input", None):
                                    ui.input(
                                        step["input"],
                                        placeholder="We need this input to proceed",
                                    ).bind_value_to(
                                        app.storage.user,
                                        # saving selection in user storage, with demo name (spaces substituted with _), step id and parameter
                                        f"input__{demo['name'].replace(' ', '_')}__{step['id']}",
                                    ).classes(
                                        "w-full"
                                    )

                                with ui.stepper_navigation():
                                    ui.button(
                                        "Run",
                                        icon="play_arrow",
                                        on_click=lambda demo=demo, step=step, pager=stepper: run_step(
                                            demo, step, pager
                                        ),
                                    ).bind_enabled_from(
                                        app.storage.user,
                                        "busy",
                                        backward=lambda x: not x,
                                    ).bind_visibility_from(step, "runner", backward=lambda x: x != "noop")
                                    ui.button(
                                        "Next",
                                        icon="fast_forward",
                                        on_click=stepper.next,
                                    ).props("color=secondary flat")
                                    ui.button(
                                        "Back",
                                        icon="fast_rewind",
                                        on_click=stepper.previous,
                                    ).props("flat").bind_visibility_from(
                                        step, "id", backward=lambda x: x != 1
                                    )  # don't show for the first step

                    if "monitors" in demo.keys():
                        for mon in demo['monitors']:
                            mon_chart = get_echart()
                            # MONITOR FUNCTION SHOULD RETURN
                            # "name": dict_item["type"],
                            # "time": dict_item["time"],
                            # "values": [
                            #     {"Tx": dict_item["tx"]},
                            #     {"Rx": dict_item["rx"]},
                            # ],
                            monitor_chart(mon, mon_chart)

    ezshow_menu.bind_value(app.storage.general["ui"], "ezshow")


# async def login():
#     app.storage.user["busy"] = True
#     response = await run.io_bound(rest.get_session)
#     if isinstance(response, Exception):
#         ui.notify(response, type='negative')
#     else:
#         if response.ok:
#             app.storage.user["cookiejar"] = response.cookies.get_dict()
#         else:
#             ui.notify(message=response.text, html=True, type="warning")
#     app.storage.user["busy"] = False


async def run_step(demo, step, pager: ui.stepper):
    app.storage.user["busy"] = True

    if step["runner"] == "rest":
        response = await run.io_bound(restrunner.post, step["runner_target"])
        if isinstance(response, Exception):
            ui.notify(response, type="negative")
        elif response.ok:
            resjson = response.json()
            # print("DEBUG RESTRUNNER", resjson)
            # ts = resjson["timestamp"] / 1000 # ignore nanoseconds precision from timestamp
            # st = resjson.get("status", None)
            # ms = resjson.get("messages", ["ERROR"]).pop()
            # er = resjson.get("errors", None)
            # ui.notify(
            #     f"{datetime.fromtimestamp(ts).strftime('%X')} : {ms if 'OK' in st else ' | '.join([e['desc'] for e in er])}",
            #     type="positive" if "OK" in st else "warning",
            # )
            # I took the lazy approach here since different rest calls have different return formats (except the 'status')
            ui.notify(
                resjson, type="positive" if resjson["status"] == "OK" else "warning"
            )
            pager.next()

        else:  # http error returned
            ui.notify(message=response.text, html=True, type="warning")

    elif step["runner"] == "restfile":
        for response in await run.io_bound(
            restrunner.postfile, DEMOS, step["runner_target"]
        ):
            if isinstance(response, Exception):
                ui.notify(response, type="negative")
            elif response.ok:
                try:
                    # logging.debug("DEBUG: RESPONSE FROM RESTRUNNER: %s", response)
                    if response.status_code == 201:
                        ui.notify("Folder created")
                    else:
                        resjson = response.json()
                        ui.notify(resjson)
                except Exception as error:
                    print(error)

                pager.next()
            else:  # http error returned
                ui.notify(message=response.text, html=True, type="warning")

    elif step["runner"] == "shell":
        ui.notify(shrunner.run_command(step["runner_target"]))
        pager.next()

    elif step["runner"] == "app":
        func = getattr(apprunner, step["runner_target"])

        if "count" in step.keys():
            # Reset the counter
            app.storage.general["demo"]["counting"] = 0
            # keep user selected count in sync
            count = app.storage.user[f"count__{demo['name'].replace(' ', '_')}__{step['id']}"]

            # add progressbar if 'count'ing
            ui.linear_progress().bind_value_from(
                app.storage.general["demo"],
                "counting",
                backward=lambda x: f"{100 * int(x/count)} %",
            )
            
            await run.io_bound(func, step["runner_parameters"], count)

        else:
            await run.io_bound(func, step["runner_parameters"])

        # pager.next()

    else:
        ui.notify(f"Would run {step['runner_target']} using {step['runner']}")
        pager.next()

    app.storage.user["busy"] = False


# Entry point for the module
def enter():
    print("EZSHOW RUNNING AS MODULE")
    ui.run(
        title="Ezlab",
        dark=None,
        native=True,
        window_size=(1024, 1024),
        # frameless=True,
        storage_secret="ezmeralr0cks",
        reload=False,
        port=native.find_open_port(),
    )


# For development and debugs
if __name__ in {"__main__", "__mp_main__"}:
    print("EZSHOW RUNNING IN DEV MODE")
    # INSECURE REQUESTS ARE OK in DEV
    requests.packages.urllib3.disable_warnings()

    ui.run(
        title="Ezshow",
        dark=None,
        native=True,
        window_size=(800, 800),
        # frameless=True,
        storage_secret="ezmeralr0cks",
        reload=True,
        port=native.find_open_port(),
    )
    logging.basicConfig(level=logging.DEBUG)

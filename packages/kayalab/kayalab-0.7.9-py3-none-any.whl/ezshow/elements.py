from nicegui import ui

import ezshow

def get_echart():
    return ui.echart(
        {
            "tooltip": {
                "trigger": "axis",
            },
            "title": {"left": 10, "text": ""},
            "legend": {"right": "center"},
            "xAxis": {
                "type": "category",
                "boundaryGap": False,
                "axisLine": {"onZero": True},
                "data": [],
            },
            "yAxis": [
                {
                    "type": "value",
                    "name": "Count",
                    "boundaryGap": [0, "100%"],
                    "splitLine": { "show": False }
                },
                {
                    "type": "value",
                    "name": "Seconds",
                    "axisLabel": {
                        "formatter": "{value} s",
                    },
                    "boundaryGap": [0, "100%"],
                    "splitLine": { "show": False }
                },
            ],
            "series": [  # manually set max series to display (TODO: find a pythonic way)
                {
                    "type": "line",
                    "smooth": True,
                    "data": [],
                },
                {
                    "type": "line",
                    "symbol": "triangle",
                    "smooth": True,
                    "data": [],
                },
                {
                    "type": "line",
                    "symbol": "roundRect",
                    "smooth": True,
                    "data": [],
                },
                {
                    "type": "line",
                    "symbol": "pin",
                    "smooth": True,
                    "data": [],
                },
            ],
        },
    )


def monitor_chart(monitor_name, monitor_chart):

    def add_metric(monitor_name, chart_name):
        t = monitor_name.split(".")
        module_name = getattr(ezshow, t[0])
        function_name = t[1]
        function_param = t[2]
        func = getattr(module_name, function_name)

        # collect the metrics
        metric = func(function_param)
        if metric:
            chart_name.options["xAxis"]["data"].append(metric["time"])
            chart_name.options["title"]["text"] = metric["name"].title()

            for idx, serie in enumerate(metric["values"]):
                chart_series = chart_name.options["series"][idx]
                for key in serie.keys():
                    if not chart_series.get("name", None):
                        chart_series["name"] = key
                    # if name ends with (s), place it onto second yAxis
                    if "(s)" in key:
                        chart_series["yAxisIndex"] = 1
                    chart_series["data"].append(int(serie[key]))
            chart_name.update()

    # Using lambda below so we capture the function name for individual steps
    timer = ui.timer(
        interval=3.0,
        callback=lambda monitor=monitor_name, chart=monitor_chart: add_metric(
            monitor, chart
        ),
        active=False,
    )
    ui.switch(
        "->".join(monitor_name.split(".")[1:]).title().replace("_", " ")
    ).bind_value(timer, "active")

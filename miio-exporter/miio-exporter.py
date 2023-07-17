from miio.device import Device
import time
from prometheus_client import Gauge, start_http_server

metrics_power = Gauge(
    "mi_plug_v3_power", "Miio plug v3 current power", ["instance", "label"]
)
metrics_temp = Gauge(
    "mi_plug_v3_temp", "Miio plug v3 current temperature", ["instance", "label"]
)

properties = [
    {"did": "MYDID", "siid": 11, "piid": 2},
    {"did": "MYDID", "siid": 12, "piid": 2},
]

mi_plug_v3_device_server = Device(
    ip="172.16.69.181", token="1b30fc9dfeb31c5027b8bf0ebf159385"
)
mi_plug_v3_device_bedroom = Device(
    ip="172.16.69.182", token="e6a7c2369ed54ba84ade78c32d1944da"
)


if __name__ == "__main__":
    start_http_server(8006)
    while True:
        ret = mi_plug_v3_device_server.send("get_properties", properties)
        metrics_power.labels(instance="172.16.69.217", label="server").set(
            ret[0]["value"]
        )
        metrics_temp.labels(instance="172.16.69.217", label="server").set(
            ret[1]["value"]
        )
        ret = mi_plug_v3_device_bedroom.send("get_properties", properties)
        metrics_power.labels(instance="172.16.69.216", label="bedroom").set(
            ret[0]["value"]
        )
        metrics_temp.labels(instance="172.16.69.216", label="bedroom").set(
            ret[1]["value"]
        )
        time.sleep(5)

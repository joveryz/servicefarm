from miio.device import Device
import json
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

config = json.load(open("/etc/config.json"))

devices = []

for device in config["devices"]:
    devices.append(Device(ip=device["ip"], token=device["token"]))

if __name__ == "__main__":
    start_http_server(8006)
    while True:
        for device in devices:
            if device.token is None or device.token == "":
                print("No token for device, will skip, ip: " + device.ip)
                continue
            try:
                ret = device.send("get_properties", properties)
            except:
                print("Error getting data from device, ip: " + device.ip)
                time.sleep(5)
                continue

            metrics_power.labels(instance=device.ip, label=device.label).set(
                ret[0]["value"]
            )
            metrics_temp.labels(instance=device.ip, label=device.label).set(
                ret[1]["value"]
            )
            time.sleep(5)

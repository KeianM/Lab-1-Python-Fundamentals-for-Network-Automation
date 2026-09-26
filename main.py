import logging
from pathlib import Path

from src.network_device import NetworkDevice
from src.parser_utils import parse_csv, parse_json, parse_xml, parse_yaml

def setup_logging():
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        filename="logs/lab.log",
        level=logging.INFO,
    )

def main():
    devices = parse_json("data/devices.json")
    yaml_data = parse_yaml("data/interfaces.yaml")
    vlans = parse_xml("data/vlans.xml")
    csv_devices = parse_csv("data/inventory.csv")

    for device in devices:
        network_device = NetworkDevice(
            device["hostname"],
            device["ip"],
            device["type"],
        )
        network_device.summarize()

    for interface in yaml_data.get("interfaces", []) if isinstance(yaml_data, dict) else []:
        msg = f"Interface {interface['name']} is {interface['status']}"
        print(msg)
        logging.info(f"INTERFACE_MSG: %s", msg)

    for device in csv_devices:
        msg = (
            f"Device {device['hostname']} is a "
            f"{device['location']} {device['role']}"
        )
        print(msg)
        logging.info(f"DEVICE_MSG: %s", msg)

    for vlan in vlans:
        msg = f"VLAN {vlan['id']} is the {vlan['name']}"
        print(msg)
        logging.info(f"VLAN_MSG: %s", msg)


if __name__ == "__main__":
    setup_logging()
    logging.info("[LAB1-START]")
    main()
    logging.info("[LAB1-END]")
import csv
import json
import logging
import xml.etree.ElementTree as ET

import yaml


def parse_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        logging.info("[PARSE_JSON_SUCCESS]")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logging.error("[PARSE_JSON_ERROR] %s", error)
        return []


def parse_yaml(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        logging.info("[PARSE_YAML_SUCCESS]")
        return data
    except (FileNotFoundError, yaml.YAMLError) as error:
        logging.error("[PARSE_YAML_ERROR] %s", error)
        return []


def parse_xml(path):
    try:
        tree = ET.parse(path)
        data = [
            {child.tag: child.text for child in vlan}
            for vlan in tree.getroot()
        ]
        logging.info("[PARSE_XML_SUCCESS]")
        return data
    except (FileNotFoundError, ET.ParseError) as error:
        logging.error("[PARSE_XML_ERROR] %s", error)
        return []


def parse_csv(path):
        try:
            with open(path, "r", encoding="utf-8", newline="") as file:
                data = list(csv.DictReader(file))
            logging.info("[PARSE_CSV_SUCCESS]")
            return data
        except (FileNotFoundError, csv.Error) as error:
            logging.error("[PARSE_CSV_ERROR] %s", error)
            return []
        
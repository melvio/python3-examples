#!/usr/bin/env python3

# <https://docs.python.org/3/library/configparser.html>
import os
from pathlib import Path
from configparser import ConfigParser


def load_file():
    config_path = Path(os.path.dirname(Path(__file__)) + '../../../data/config_file.conf').resolve()
    assert config_path.exists(), "File does not exists"
    return config_path


config_file = load_file()
config_parser = ConfigParser()
files = config_parser.read(config_file)
assert len(files) == 1 and Path(files[0]).exists(), "expected to load only 1 file"

configparser = ConfigParser()
configparser.read(config_file)
print(configparser["contactdetails"])
# <Section: contactdetails>
print(configparser["contactdetails"].get("name"))
# William Stewart Halsted
print(configparser["contactdetails"].get("email"))
# he.probably.will.not.reply@email.com

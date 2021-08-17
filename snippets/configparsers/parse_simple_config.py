#!/usr/bin/env python3

# <https://docs.python.org/3/library/configparser.html>
from pathlib import Path
from configparser import ConfigParser

config_file = Path("../../data/config_file.conf").resolve()
assert config_file.exists(), "File does not exists"

configparser = ConfigParser()
configparser.read(config_file)
print(configparser["contactdetails"])
# <Section: contactdetails>
print(configparser["contactdetails"].get("name"))
# William Stewart Halsted
print(configparser["contactdetails"].get("email"))
# he.probably.will.not.reply@email.com




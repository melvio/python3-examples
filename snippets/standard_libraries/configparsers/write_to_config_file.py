#!/usr/bin/env python3

import os
import shutil
from pathlib import Path
import configparser
from configparser import ConfigParser


def get_conf_file():
    dirname: Path = Path(os.path.dirname(__file__)).parent
    config_file: Path = dirname / 'innovation_file.conf'
    assert config_file.exists() and config_file.is_file(), f"Expected {config_file} to exists"
    return config_file


def create_copy_of_conf_file(file: Path, copy_name='copy.conf') -> Path:
    """
    Create a copy and return the copy to write to.
    In this manner, we keep the original untouched
    """
    copy_path: Path = file.parent / copy_name
    shutil.copyfile(file, copy_path)
    return copy_path.resolve()


def get_parser(file: Path):
    parser = ConfigParser()
    files = parser.read(file)
    assert len(files) == 1 and Path(files[0]).exists(), f"expected {files} to have 1 existing file"
    return parser


copy_file: Path = create_copy_of_conf_file(get_conf_file())
config_parser = get_parser(copy_file)
print(config_parser.sections())

innovation_2020_section = config_parser["innovation_price_2020"]


def print_section_values(section):
    for value in section.values():
        print(f"value={value}")
        # value="Wolk Heupairbag"


print_section_values(innovation_2020_section)

# adding an key-value pair to the innovation_price_2020 section:
innovation_2020_section["place2"] = "Indicatieloze dagbesteding"
with open(copy_file, "w") as updated_file:
    config_parser.write(updated_file)


def print_section_values(section):
    for value in section.values():
        print(f"value={value}")
        # value="Wolk Heupairbag"
        # value=Indicatieloze dagbesteding


print_section_values(innovation_2020_section)

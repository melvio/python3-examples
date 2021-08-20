#!/usr/bin/env python3


import os
from pathlib import Path
from configparser import ConfigParser

test_file = Path(os.path.dirname(Path(__file__).resolve()) + '/innovation_file.conf')
config_parser = ConfigParser()
files = config_parser.read(test_file)
assert len(files) == 1 and Path(files[0]).exists(), "expected to load only 1 file"

print("sections", config_parser.sections())


section_2019 = config_parser["innovation_price_2019"]
section_2020 = config_parser["innovation_price_2020"]
winner_public_jury = section_2019["winner_public_jury"]
print(winner_public_jury)  # "PinkTrainer"
print(type(winner_public_jury))  # <class 'str'>

# watch out: everything is interpreted as a string:
winner_public_jury_price = section_2019["winner_public_jury_price_euros"]
print(winner_public_jury_price)  # 5000
print(type(winner_public_jury_price))  # <class 'str'>

# to get around that:
winner_public_price_int = section_2019.getint("winner_public_jury_price_euros")
print(winner_public_price_int)  # 5000
print(type(winner_public_price_int))  # <class 'int'>


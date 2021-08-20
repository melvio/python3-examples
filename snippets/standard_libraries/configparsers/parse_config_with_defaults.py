import os
from pathlib import Path
from configparser import ConfigParser

config_file = Path(os.path.dirname(Path(__file__).resolve()) + '/innovation_file.conf')
assert config_file.exists(), f"Expected {config_file} to exists"

config_parser = ConfigParser()
config_parser.read(config_file)

section_2020 = config_parser["innovation_price_2020"]


# getting defaults, in case something is missing
try:
    print(section_2020["does not exist"])
except KeyError as e:
    print('KeyError', e)  # KeyError 'does not exist'

print(section_2020.get("does not exist"))  # None

print(section_2020.get("does not exist", fallback="unknown"))  # "unknown"

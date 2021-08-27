#!/usr/bin/env python3

# source:
# https://docs.python.org/3/library/pprint.html#example

import json
import pprint
from urllib.request import urlopen

with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

# pprint.pprint(project_info)
# print(type(project_info))


print(json.dumps(project_info))

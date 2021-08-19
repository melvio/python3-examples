#!/usr/bin/env python2
import json

data = {"key1": [1, 2, 3], "key2": "value"}
print(json.dumps(data))
# '{"key1": [1, 2, 3], "key2": "value"}'

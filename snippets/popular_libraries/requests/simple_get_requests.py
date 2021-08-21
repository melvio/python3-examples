#!/usr/bin/env python3
import requests
from requests import Response

url = "https://raw.githubusercontent.com/melvio/python3-examples/main/data/mock_data.json"
response: Response = requests.get(url=url)

print(response.text)
# nicely formatted response body

print(response.status_code)
# 200

print(response.ok)
# True

print(response.headers)
# {'Connection': 'keep-alive', ... 'Content-Encoding': 'gzip', ... 'Source-Age': '124'}

print(response.json())
# {'_created-at': '2021-08-15T17:30:04', 'username': 'melvio', 'age': 28, 'hobbies': ['reading', 'exercise'], 'powerlifting-prs': ... }

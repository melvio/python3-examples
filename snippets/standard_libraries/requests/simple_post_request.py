#!/usr/bin/env python3
import requests
from requests import Response

# Using httpbin.org: <https://stackoverflow.com/questions/5725430/http-test-server-accepting-get-post-requests#9770981>
url = "https://httpbin.org/anything"
query_params = dict(amount=5, say="hello")
body_payload = dict(country="US", currency="$")
headers = {"x-some-header": "hiyaa"}
response: Response = requests.post(url,
                                   json=body_payload,
                                   headers=headers,      # headers are appended to default HTTP headers
                                   params=query_params)  # params are query params and will be baked into the "url": "https://httpbin.org/anything?amount=5&say=hello"

# .text contains the body of the response
print(response.text)

# .json() parses json and returns it as a dict if possible
print(response.json())

# response headers
print(response.headers)

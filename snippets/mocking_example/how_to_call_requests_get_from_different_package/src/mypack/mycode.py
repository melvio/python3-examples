#!/usr/bin/env python3

import requests


def good_response(url):
    r = requests.get(url)

    # You can better us r.ok here. But this is for the example
    ok = 200
    if r.status_code == ok:
        print(r.json())
        return True

    not_ok = 404
    if r.status_code == not_ok:
        print(r.json())
        return False






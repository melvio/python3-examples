#!/usr/bin/env python3

from requests import get


def get_content(url):
    r = get(url)
    if r.status_code == 200:
        return r.content
    return "oeps"

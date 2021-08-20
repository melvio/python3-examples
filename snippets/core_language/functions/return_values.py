#!/usr/bin/env python3


def add_to_dict(start_dict: dict):
    start_dict["more_wups"] = "Worldcom"
    return start_dict


start_value = {"wups": "Theranos"}
print(start_value)
return_value = add_to_dict(start_value)
print(start_value)  # start_value has been modified too
print(return_value)

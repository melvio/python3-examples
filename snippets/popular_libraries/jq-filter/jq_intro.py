#!/usr/bin/env python3

import jq

IDENTITY_FILTER = "."

jq_compile = jq.compile(IDENTITY_FILTER)
print(jq_compile.input("hello").first())  # hello
print(jq_compile.input(["hello", "there"]).first())  # ['hello', 'there']
print(jq_compile.input({"hello": ["there", "all"]}).first())  # {'hello': ['there', 'all']}




#!/usr/bin/env python3

import jq

IDENTITY_FILTER = "."

jq_compile = jq.compile(IDENTITY_FILTER)
print(jq_compile.input("hello").first())
print(jq_compile.input(["hello", "there"]).first())
print(jq_compile.input({"hello": ["there", "all"]}).first())

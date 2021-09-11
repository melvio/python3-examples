#!/usr/bin/env python3
import jq

jq_filter = jq.compile(".")

print(jq_filter.input(["a", "b", "c"]).first())  # ['a', 'b', 'c']
print(jq_filter.input(["a", "b", "c"]).all())    # [['a', 'b', 'c']]

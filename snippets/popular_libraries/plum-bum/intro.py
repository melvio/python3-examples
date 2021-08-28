#!/usr/bin/env python3


from plumbum.cmd import echo

pseudo_json = {'hi': 'there'}
cmd = echo[pseudo_json]  # /usr/bin/echo {'hi': 'there'}
print(cmd)
print(cmd())  # {'hi': 'there'}

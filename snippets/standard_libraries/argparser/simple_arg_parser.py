#!/usr/bin/env python3

import sys
from argparse import ArgumentParser

prog_name = f"normally I'm called {sys.argv[0]} but the 'prog' parameter has overridden that.\n   this_command.py"
description = "I will store your arguments and print them in a sorted order"
argument_parser = ArgumentParser(prog=prog_name, description=description)

argument_parser.add_argument("words", type=str, nargs="+")

arguments = argument_parser.parse_args()
supplied_words = arguments.words
print(sorted(supplied_words))

# $ ./simple_arg_parser.py word letter char
# ['char', 'letter', 'word']

# integers are interpreted to be strings:
# $ ./simple_arg_parser.py 20 100 1
# ['1', '100', '20']

# you must at least supply 1 argument:
# ./simple_arg_parser.py
# usage: normally I'm called ./simple_arg_parser.py but the 'prog' parameter has overridden that.
#   this_command.py [-h] words [words ...]
# normally I'm called ./simple_arg_parser.py but the 'prog' parameter has overridden that.
#   this_command.py: error: the following arguments are required: words

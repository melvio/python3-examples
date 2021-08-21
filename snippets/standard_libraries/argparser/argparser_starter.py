#!/usr/bin/env python3

# <https://docs.python.org/3/library/argparse.html>

from argparse import ArgumentParser

parser = ArgumentParser(description="some parser")

print(parser.description)  # some parser

parser.print_usage()  # usage: parse_simple_args.py [-h]

parser.usage = "just call this command"

parser.print_usage()  # usage: just call this command

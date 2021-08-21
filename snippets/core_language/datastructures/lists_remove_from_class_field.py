#!/usr/bin/env python3
# https://docs.python.org/3/tutorial/datastructures.html#
from typing import List


class HelpParser:
    def __init__(self, *, cmdline_args: List[str]):
        self.cmdline_args = cmdline_args

    def __str__(self) -> str:
        return f"HelpParser(cmdline_args={self.cmdline_args})"

    def parse_global_options(self):
        for argument in self.cmdline_args:
            longhelp = "--help"
            shorthelp = "-h"
            if argument == longhelp:
                self.cmdline_args.remove(longhelp)
            elif argument == shorthelp:
                self.cmdline_args.remove(shorthelp)


cmdline = ["ls", "--help"]
help_parser = HelpParser(cmdline_args=cmdline)
print(help_parser)  # HelpParser(cmdline_args=['ls', '--help'])
help_parser.parse_global_options()
print(help_parser)  # HelpParser(cmdline_args=['ls'])

cmdline2 = ["git", "-h", "status"]
help_parser2 = HelpParser(cmdline_args=cmdline2)
print(help_parser2)  # HelpParser(cmdline_args=['git', '-h', 'status'])
help_parser2.parse_global_options()
print(help_parser2)  # HelpParser(cmdline_args=['git', 'status'])

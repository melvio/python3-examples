#!/usr/bin/env python3

import click


@click.command()
@click.option("--count", "-c", default=1, help="number of pills")
@click.argument("pill-name")
def count_pills(count, pill_name):
    for i in range(count):
        print(f"counted {i + 1} {pill_name} pills")


if __name__ == "__main__":
    count_pills()

# ./click_with_option.py --help
# Usage: click_with_option.py [OPTIONS] PILL_NAME

# Options:
#   -c, --count INTEGER  number of pills
#   --help               Show this message and exit.


# ./click_with_option.py Paracetamol

# ./click_with_option.py -c3 Ibuprofen
# counted 1 Ibuprofen pills
# counted 2 Ibuprofen pills
# counted 3 Ibuprofen pills

#!/usr/bin/env python3
import click
import random


@click.command()
@click.option('--total', default=2, help='Number of docters to output.')
def doctor(total):
    """ Basic method will return a random docter"""
    for number in range(total):
        print(random.choice(['orthopedist', 'cardiologist', 'radiologist', 'pediatrician',
                             'neurosurgeon']))


if __name__ == '__main__':
    doctor.main(standalone_mode=False)
    print("HERE1")  # HERE1

    doctor()
    print("HERE2")  # "" (empyt)

#!/usr/bin/env python3
import click


@click.command()
@click.argument("dose", type=click.FLOAT)
def give_dose(dose: float):
    if dose >= 1.9:
        raise click.ClickException("Dosage Too High")
    click.echo(f"Gave: {dose:4.3f}ml")


if __name__ == "__main__":
    give_dose()
# $ python3 raising_clickex.py 2
# Error: Dosage Too High

# $ python3 raising_clickex.py 1
# Gave: 1.000ml

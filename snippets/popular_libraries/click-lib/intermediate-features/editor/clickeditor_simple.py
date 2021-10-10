#!/usr/bin/env python3
import click


def promp_user_with_editor(old_param: str) -> str:
    comment = "# Edit domain Name:\n"
    editor_content = f"{comment}{old_param}"
    result = click.edit(editor_content)
    # In real code, you would do some error checking here.
    new_param = result.split(comment)[1].strip()
    return new_param


@click.command()
def main():
    new_param = promp_user_with_editor(old_param="testdomain.com")
    click.echo(f"{new_param=}")


if __name__ == "__main__":
    main()

import click

user_input = click.prompt(text="Folder name", default="Download")
print(f"{user_input=}")

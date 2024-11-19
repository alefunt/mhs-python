import sys

import click


@click.command()
@click.argument("number_of_lines", required=False, default=10, type=int)
@click.option("--no-trailing-newline", is_flag=True, help="Do not add a trailing newline")
def generate_newlines(number_of_lines: int, no_trailing_newline: bool):
    for _ in range(number_of_lines - 1):
        sys.stdout.write('|\n')
    sys.stdout.write('|')
    if not no_trailing_newline:
        sys.stdout.write('\n')


if __name__ == "__main__":
    generate_newlines()

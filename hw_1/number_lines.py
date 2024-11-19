import sys

import click


def pad_n(i):
    return str(i).rjust(6, ' ') + '\t'


def number_lines_impl(source):
    for i, line in enumerate(source, start=1):
        print(f'{pad_n(i)}{line[:-1]}')


@click.command()
@click.argument("file", type=click.Path(exists=True), required=False)
def number_lines(file):
    """Numbers the lines of a given file

    If file is not passed reads from stdin
    """
    if file:
        with open(file, 'r') as f:
            number_lines_impl(f)
    else:
        number_lines_impl(sys.stdin)


if __name__ == "__main__":
    number_lines()

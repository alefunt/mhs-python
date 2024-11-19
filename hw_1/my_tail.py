import sys

import click


def tail_impl(source, n=10):
    buffer = []
    p = 0
    for i, line in enumerate(source):
        if len(buffer) < n:
            buffer.append(line)
        else:
            buffer[p] = line
            p = (p + 1) % n


    start_index = p % n if len(buffer) == n else 0
    for i in range(len(buffer)):
        print(buffer[(start_index + i) % len(buffer)], end='')


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True), required=False)
def my_tail(files):
    """Returns last 10 lines of a given file

    If file is not passed returns last 17 lines from stdin
    """
    if files:
        if len(files) == 1:
            with open(files[0], 'r') as f:
                tail_impl(f)
        else:
            for i, file in enumerate(files):
                if i != 0:
                    print()
                print(f'=> {click.format_filename(file)} <=')
                with open(file, 'r') as f:
                    tail_impl(f)
    else:
        tail_impl(sys.stdin, 17)


if __name__ == "__main__":
    my_tail()

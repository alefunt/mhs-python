import sys

import click


def tail_impl(source):
    total_lines = 0
    total_words = 0
    total_bytes = 0
    for line in source:
        total_lines += 1
        total_words += len(line.split())
        total_bytes += len(line.encode('utf-8'))
    return total_lines, total_words, total_bytes


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True), required=False)
def word_count(files):
    """Returns line count, word count, byte count for given files

    If file is not passed returns statistics for stdin
    """
    if files:
        if len(files) == 1:
            with open(files[0], 'r') as f:
                lines, words, byte = tail_impl(f)
                print(lines, words, byte, click.format_filename(files[0]))
        else:
            total_lines = 0
            total_words = 0
            total_bytes = 0
            for i, file in enumerate(files):
                with open(file, 'r') as f:
                    lines, words, byte = tail_impl(f)
                    total_lines += lines
                    total_words += words
                    total_bytes += byte
                    print(lines, words, byte, click.format_filename(file))
            print(total_lines, total_words, total_bytes, "total")
    else:
        lines, words, byte = tail_impl(sys.stdin)
        print(lines, words, byte)


if __name__ == "__main__":
    word_count()

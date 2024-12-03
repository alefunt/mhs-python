def _begin_tabular(n_cols: int):
    return f"\\begin{{tabular}}{{|{'|'.join(['c' for _ in range(n_cols)])}|}}"


def _end_tabular():
    return "\\end{tabular}"


def _table_row(row: tuple):
    return f"{' & '.join([str(v) for v in row])} \\\\"


def _hline():
    return "\\hline"


def join_list(separator: str, rows: list[str]):
    if len(rows) == 0: return
    result = [rows[0]]
    for row in rows[1:]:
        result += [separator, row]
    return result


def create_table(data: list[list]):
    if len(data) < 1: return ""
    result = [_begin_tabular(len(data)), _hline()]

    rows = [_table_row(row) for row in zip(*data)]
    result += join_list(_hline(), rows)

    result.append(_hline())
    result.append(_end_tabular())

    return "\n".join(result)

import datetime
import logging
import math
import timeit
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

from tabulate import tabulate

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def split(size, n):
    """Split the interval [0, size) in n parts with closest to equal sizes.
    Returns
    -------
    list[tuple[int, int]]
        a list of tuples (start, size)
    """
    k, m = divmod(size, n)
    return [(i * k + min(i, m), k + min(i + 1, m) - min(i, m)) for i in range(n)]


def sub_integrate(f, a, step, n_iter):
    logging.debug(f"Starting sub integration [{a}+={step}<{n_iter}],")
    acc = 0
    for i in range(n_iter):
        acc += f(a + i * step) * step
    logging.debug(f"Ending sub integration [{a}+={step}<{n_iter}], result = {acc}")
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000,
              executor: [ThreadPoolExecutor | ProcessPoolExecutor] = ThreadPoolExecutor):
    logging.debug(f"Starting integration with {n_jobs} jobs")
    acc = 0
    step = (b - a) / n_iter

    chunks = split(n_iter, n_jobs)

    with executor(max_workers=n_jobs) as ex:
        futures = [ex.submit(sub_integrate, f, a + step * start, step, n) for (start, n) in chunks]
        for future in futures:
            acc += future.result()

    logging.debug(f"Ending integration with {n_jobs} jobs, result = {acc}")
    return acc


def integrate_old(f, a, b, *, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def measure(func):
    n_tests = 1
    return datetime.timedelta(seconds=timeit.timeit(func, number=n_tests) / n_tests)


def test(f, a, b, n_jobs):
    proc_time = measure(lambda: integrate(f, a, b, n_jobs=n_jobs, executor=ProcessPoolExecutor))
    thread_time = measure(lambda: integrate(f, a, b, n_jobs=n_jobs, executor=ThreadPoolExecutor))

    return [n_jobs, proc_time, thread_time]


if __name__ == '__main__':
    f = math.cos
    a = 0
    b = math.pi / 2

    print(tabulate([test(f, a, b, n) for n in range(10, 11)], headers=["n_jobs", "proc", "thread"]))
    print(f"Base time:{measure(lambda: integrate_old(f, a, b))}")

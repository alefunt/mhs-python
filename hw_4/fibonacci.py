import datetime
import timeit
from multiprocessing import Process
from threading import Thread

from tabulate import tabulate


def fibonacci(n):
    if n == 0: return 0
    if n < 2: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_seq(n, n_times):
    for _ in range(n_times):
        fibonacci(n)


def fib_thread(n, n_times):
    threads = []
    for _ in range(n_times):
        thread = Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def fib_proc(n, n_times):
    procs = []
    for _ in range(n_times):
        process = Process(target=fibonacci, args=(n,))
        procs.append(process)
        process.start()
    for process in procs:
        process.join()


def test(n, n_times, n_tests):
    seq_time = timeit.timeit(lambda: fib_seq(n, n_times), number=n_tests)
    thread_time = timeit.timeit(lambda: fib_thread(n, n_times), number=n_tests)
    proc_time = timeit.timeit(lambda: fib_proc(n, n_times), number=n_tests)
    return [datetime.timedelta(seconds=seq_time / n_times),
            datetime.timedelta(seconds=thread_time / n_times),
            datetime.timedelta(seconds=proc_time / n_times)]


def main():
    results = []
    for i in range(5, 36, 5):
        results.append([i, *test(i, 10, 10)])

    print(tabulate(results, headers=["N", "seq_time", "thread_time", "proc_time"]))


if __name__ == '__main__':
    main()

import codecs
import logging
import multiprocessing as mp
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def proc_a(inp, queue):
    while True:
        received = inp.recv()
        logging.debug(f"A received '{received}'")

        queue.put(received.lower())


def proc_b(in_queue, out_queue):
    while True:
        received = in_queue.get()
        # Technically it was received immediately,
        # don't know how to make it without some kind of buffer
        logging.debug(f"B received '{received}'")

        encoded = codecs.encode(received, 'rot_13')

        print(encoded)
        out_queue.put(encoded)

        time.sleep(5)


def main_queue_listener(queue):
    while True:
        logging.debug(f"Main received '{queue.get()}'")


def main():
    usr_in, a_in = mp.Pipe()
    a_b_queue = mp.Queue()
    b_usr_queue = mp.Queue()

    a = mp.Process(target=proc_a, args=(a_in, a_b_queue,))
    b = mp.Process(target=proc_b, args=(a_b_queue, b_usr_queue,))

    mp.Process(target=main_queue_listener, args=(b_usr_queue,)).start()  # just for non-blocking logging from main

    a.start()
    b.start()

    while True:
        usr_in.send(input())


if __name__ == '__main__':
    main()

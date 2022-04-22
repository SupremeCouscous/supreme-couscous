~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from multiprocessing import Process, Pipe
import time

fruits = ['apple', 'banana', 'citron', 'pineapple', 'kiwi', 'orange']


def worker1(c):
    for i in range(10):
        time.sleep(2)
        print("send a message")
        c.send([i, fruits[i % 6]])
    c.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=worker1, args=(child_conn,))
    p.start()
    for _ in range(10):
        time.sleep(3)
        print(parent_conn.recv())
    p.join()
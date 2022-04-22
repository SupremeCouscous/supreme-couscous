from multiprocessing import Process, Queue
import time

stores = ['7-11', 'fami', 'star-bucks']


def f(q):
    for i in range(10):
        time.sleep(2)
        q.put((stores[i % 3], (i+1) * 10))


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()

    for _ in range(10):
        print(q.get())
    # p.join()
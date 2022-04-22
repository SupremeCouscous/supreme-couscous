import time
from multiprocessing import Process

COUNT = 50000000


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1


if __name__ == '__main__':
    start = time.perf_counter()
    p1 = Process(target=countdown, args=(COUNT // 4,))
    p2 = Process(target=countdown, args=(COUNT // 4,))
    p3 = Process(target=countdown, args=(COUNT // 4,))
    p4 = Process(target=countdown, args=(COUNT // 4,))
    processes = [p1, p2, p3, p4]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    end = time.perf_counter()

    print("total time in seconds:", end - start)
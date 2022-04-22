import time
from threading import Thread

COUNT = 50000000


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1


t1 = Thread(target=countdown, args=(COUNT // 4,))
t2 = Thread(target=countdown, args=(COUNT // 4,))
t3 = Thread(target=countdown, args=(COUNT // 4,))
t4 = Thread(target=countdown, args=(COUNT // 4,))

start = time.perf_counter()
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
end = time.perf_counter()

print("total time in seconds:", end - start)
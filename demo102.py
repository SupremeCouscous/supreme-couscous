import multiprocessing
import time
import random

def worker(num, waiting_second):
    print(f"[{num}] start to work")
    time.sleep(waiting_second)
    print(f"[{num}] finish work")

if __name__ == '__main__':
    jobs = []
    for i in range(10):
        print("now prepare work:%d" % i)
        p = multiprocessing.Process(target=worker, args=("part%d" % i, random.randint(1, 10)))
        jobs.append(p)
        p.start()
    print("jobs=", jobs)
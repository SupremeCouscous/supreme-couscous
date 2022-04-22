import multiprocessing
import time


def worker():
    print("...start working...")
    time.sleep(2)
    print("...stop working...")
    return


if __name__ == '__main__':
    jobs = []
    for i in range(10):
        print("now execute part:%d" % i)
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    print("jobs result=", jobs)
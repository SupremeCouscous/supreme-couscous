from multiprocessing import Pool
import time

COUNT = 50000000


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1


if __name__ == '__main__':
    pool = Pool(processes=4)
    start = time.perf_counter()
    r1 = pool.apply_async(countdown, [COUNT // 4])
    r2 = pool.apply_async(countdown, [COUNT // 4])
    r3 = pool.apply_async(countdown, [COUNT // 4])
    r4 = pool.apply_async(countdown, [COUNT // 4])
    pool.close()
    pool.join()
    # countdown(COUNT)
    end = time.perf_counter()

    print("total time in seconds:", end - start)
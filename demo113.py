import time

COUNT = 50000000


def countdown(n):
    global COUNT
    for i in range(n):
        COUNT -= 1


start = time.perf_counter()
countdown(COUNT)
end = time.perf_counter()

print("total time in seconds:", end - start)
import multiprocessing, time


def worker():
    n = multiprocessing.current_process().name
    print(f"[{n}]start to work")
    time.sleep(5)
    print(f"[{n}]finish work")

def dworker():
    n = multiprocessing.current_process().name
    print(f"[{n}]start to work")
    time.sleep(8)
    print(f"[{n}]finish work")


if __name__ == '__main__':
    d1 = multiprocessing.Process(name="daemon1", target=dworker)
    d1.daemon = True

    d2 = multiprocessing.Process(name="non daemon, normal", target=worker)
    d2.daemon = False

    d1.start()
    d2.start()
    # time.sleep(6)
    d1.join()
    print("main process terminated")
import multiprocessing, time


def worker():
    name = multiprocessing.current_process().name
    print(f"{name}: start working")
    time.sleep(2)
    print(f"{name}: stop working")


def service():
    name = multiprocessing.current_process().name
    print(f"{name}: start working")
    time.sleep(6)
    print(f"{name}: stop working")


if __name__ == '__main__':
    s1 = multiprocessing.Process(target=service, name="gc_service")
    s2 = multiprocessing.Process(target=service, name="backup_service")
    w1 = multiprocessing.Process(target=worker)
    w2 = multiprocessing.Process(target=worker, name="download work")
    w3 = multiprocessing.Process(target=worker)
    processes = [s1, s2, w1, w2, w3]
    for p in processes:
        p.start()
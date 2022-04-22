import multiprocessing
import time

def daemon():
    n = multiprocessing.current_process().name
    print(f"[{n}]start to work as daemon")
    time.sleep(2)
    print(f"[{n}]stop work as daemon")

def non-daemon()
    n = multiprocessing, current_process().name
    print(f"[{n}]start to work as non daemon")
    time.sleep(1)
    print(f"[{n}stop work as non daemon")

if __name__ == '__main__':
    d1 = multiprocessing.Process(name="daemon", target=daemon)
    d1.daemon = True
    d2 = multiprocessing.Process(name="worker", target=non_daemon)
    d2.daemon = False
    print('d1, d2 is alive?')
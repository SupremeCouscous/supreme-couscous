import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        for i in range(10):
            time.sleep(2)
            print("do something in part:%d" % i)
w1 = WorkerThread()
w2 = WorkerThread()
w1.start()
w2.start()
w1.join()
w2.join()

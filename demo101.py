import multiprocessing

def worker():
    print("...working...")
    return

if __name__=='__main__':
    jobs = []
    for i in range(10):
        print("now execute part:%d" % i)
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    print("jobs result=", jobs)
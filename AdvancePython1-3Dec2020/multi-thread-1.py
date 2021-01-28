#multi threading
import threading
def job1():
    print("Job 1 started")
    for i in range(10000):
        for j in range(10000):
            k = i+j
    print("Job_1 done")


def job2():
    print("Job 2 started")
    for i in range(100):
        for j in range(10):
            k = i+j
    print("Job_2 done")


def job3():
    print("Job 3 started")
    for i in range(10):
        for j in range(5):
            k = i+j
    print("Job_3 done")

worker_1 = threading.Thread(target=job1)
worker_2 = threading.Thread(target=job2)
worker_3 = threading.Thread(target=job3)

worker_1.start()
worker_2.start()
worker_3.start()

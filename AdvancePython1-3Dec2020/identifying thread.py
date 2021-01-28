import threading
import time
#identifying 
def job():
    print("job started by {}".format(threading.current_thread().getName()))
    time.sleep(2)
    for i in range(1000):
        for j in range(1000):
            k=i+j
    print("job ended by {}".format(threading.current_thread().getName()))


print("cuurent==>",threading.current_thread().getName())

for i in range(5):
    t  = threading.Thread(target=job,name='Thread_{}'.format(i))
    t.start()

import logging
import time
import threading

logging.basicConfig(level = logging.DEBUG,format='[%(levelname)s] (%(threadName)s)  %(message)s')

def job():
    logging.debug('Starting.......')
    time.sleep(2)
    logging.debug('Exiting')

for i in range(3):
    th = threading.Thread(target=job,name=f'thread_{i}')
    th.start()

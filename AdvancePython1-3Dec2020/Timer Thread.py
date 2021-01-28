import logging
import threading
import time
logging.basicConfig(level = logging.DEBUG,format='[%(levelname)s] (%(threadName)s)  %(message)s')

def delayed():
    logging.debug('Running')

t1 = threading.Timer(3,delayed)
t1.setName('thread-->1')


t2 = threading.Timer(1,delayed)
t2.setName('thread-->2')

logging.debug('Starting timer threads...')
t1.start()
t2.start()

time.sleep(5)
logging.debug('cancelling {}'.format(t2.getName()))

t2.cancel()

logging.debug('Done')

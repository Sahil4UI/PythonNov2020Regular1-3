import logging
import threading

logging.basicConfig(level = logging.DEBUG,format='[%(levelname)s] (%(threadName)s)  %(message)s')

class MyThread(threading.Thread):
    def __init__(self,group=None,target=None,name=None,args=(),*,daemon=None):
        super().__init__(group=group,target=target,name=name)
        self.args = args
    
    def run(self):
        logging.debug('Running with i=%s '%(self.args))


for i in range(10):
    obj = MyThread(args=(i,))
    obj.start()

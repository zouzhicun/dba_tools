# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 调用semaphone限制资源的并发访问

import logging
import threading
import random
import time

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s (%(threadName)-2s) %(message)s',
    
)

class ActivePool(object):
    def __init__(self):
        super(ActivePool,self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self,name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s',self.active)
    def makeInactive(self,name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running：%s',self.active)

def worker(s,pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(target=worker,name=str(i),args=(s,pool))
    t.start()







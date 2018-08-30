# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 定时器线程，调用Timer方法。

import logging
import threading
import time

logging.basicConfig(
	level = logging.DEBUG,
	format = '[%(levelname)s] (%(threadName)-10s) %(message)s',
	
)

def delayed():
	logging.debug('worker running')
	return 


t1 = threading.Timer(3,delayed)
t1.setName('t1')
t2 = threading.Timer(3,delayed)
t2.setName('t2')

logging.debug('worker running')
t1.start()
t2.start()


logging.debug('waiting before canceling %s',t2.getName())
time.sleep(2)
logging.debug('canceling %s',t2.getName())
t2.cancel()
logging.debug('done')


#-*- coding: UTF-8 -*-

import Queue
import threading
import time
queue = Queue.Queue()

class ThreadQueue(threading.Thread):
    """Threaded job"""
    def __init__(self, queue,worktype=None):
        threading.Thread.__init__(self)
        self._queue = queue
        self._work_type = worktype  #线程ID
    def run(self):
        while True:  
            self._process_job(self._queue.get(),self._work_type)
            time.sleep(1)                
            self._queue.task_done()  #退出
                
            
            
    def _process_job(self,job,worker):
    	print '--->',job,'worker==',worker


def main():
#spawn a pool of threads, and pass them queue instance
    for i in range(12):
        t = ThreadQueue(queue,i)
        t.setDaemon(True)
        t.start()
        #populate queue with data
    for host in xrange(1,10,2):  #往线程中填充数据
        queue.put(host)   #插入队列
    #wait on the queue until everything has been processed
    queue.join()
    
main()
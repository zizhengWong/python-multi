""" 
信号量用来控制线程并发数
"""
import threading
import time

semaphore = threading.Semaphore(5)

def func():
    if semaphore.acquire():
        print (threading.currentThread().getName() + '获取共享资源')
        time.sleep(2)
        print(threading.currentThread().getName() + '释放共享资源')
        semaphore.release()

for i in range(10):
  t1 = threading.Thread(target=func)
  t1.start()

""" 
pool map()方法, 在爬虫的领域里也可以使用
pool = Pool()
pool.map(creat_thumbnail, images) #关键点，images是一个可迭代对象
pool.close()
pool.join()
"""
from  multiprocessing import Process,Pool
import os, time, random

def fun1(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    pool = Pool(5) #创建一个5个进程的进程池

    for i in range(10):
        pool.apply_async(func=fun1, args=(i,))

    pool.close() # 调用close()之后就不能继续添加新的Process了
    pool.join()
    print('结束测试')
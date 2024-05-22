""" 
通过内部维护counter来避免dead lock
直到一个线程所有的acquire都被release，其他的线程才能获得资源

当某个线程内部多次调用可重入锁时，仅仅在第一次获取锁对象时调用了_thread模块中锁的acquire()方法，
第二次，第三次...只是让计数器加1了而已；而当其他线程获取该锁时，
因为调用了 _trhead模块中 _allocate_lock()方法阻塞了自己。
"""
import threading
import time

lock = threading.RLock()  #递归锁


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):

        lock.acquire()  # 如果锁被占用,则阻塞在这里,等待锁的释放

        print ("线程 %s , 想拿: %s--%s" %(self.name, "苹果",time.ctime()))

        lock.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "香蕉",time.ctime()))
        lock.release()
        lock.release()


    def fun2(self):

        lock.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "香蕉",time.ctime()))
        time.sleep(0.1)

        lock.acquire()
        print ("线程 %s , 想拿: %s--%s" %(self.name, "苹果",time.ctime()))
        lock.release()

        lock.release()

if __name__ == "__main__":
    for i in range(0, 10):  #建立10个线程
        my_thread = MyThread()  #类继承法是python多线程的另外一种实现方式
        my_thread.start()
""" 
num的正确结果应该是0
问题在于当第一个线程sleep 0.001秒这个期间，这个线程会做yield操作，就是把cpu切换给别的线程执行。
等到后面cpu重新切换给线程1，线程2，线程3上执行的时候，他们执行减1操作后，其实等到的num其实都是99，而不是顺序递减的。
"""
import threading
import time

num = 100

def fun_sub():
    global num
    # num -= 1
    num2 = num
    time.sleep(0.001)
    num = num2-1

if __name__ == '__main__':
    print('开始测试同步锁 at %s' % time.ctime())

    thread_list = []
    for thread in range(100):
        t = threading.Thread(target=fun_sub)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()
    print('num is %d' % num)
    print('结束测试同步锁 at %s' % time.ctime())
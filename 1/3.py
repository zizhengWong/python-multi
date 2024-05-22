""" 
这里如果设置t1为Daemon，那么主线程就不管t1的运行状态，只管等待t2结束， t2结束主线程就结束了
因为t2的时间4秒，t1的时间2秒，主线程在等待t2线程结束的过程中，t1线程自己结束了，
"""
import threading
import time

def say(name):
        print('你好%s at %s' %(name,time.ctime()))
        time.sleep(2)
        print("结束%s at %s" %(name,time.ctime()))

def listen(name):
    print('你好%s at %s' % (name,time.ctime()))
    time.sleep(4)
    print("结束%s at %s" % (name,time.ctime()))

if __name__ == '__main__':
    t1 = threading.Thread(target=say,args=('tony',))  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
    t1.setDaemon(True)
    t1.start() #线程执行
    t2 = threading.Thread(target=listen, args=('simon',)) #这里就是创建了一个线程对象t2
    t2.start()

    print("程序结束=====================")
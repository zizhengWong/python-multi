""" 
Queue是线程安全的队列实现, 用来在生产者和消费者线程之间的信息传递

下面可以看出，list列表是不是线程安全的
"""
import threading,time

m=[1,2,3,4,5]
print(m[-1])

def remove_last():
    a=m[-1]
    time.sleep(1)
    m.remove(a)


t1=threading.Thread(target=remove_last)
t1.start()

t2=threading.Thread(target=remove_last)
t2.start()
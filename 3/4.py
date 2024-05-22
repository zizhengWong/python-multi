""" 
创建一个“队列”对象
import Queue
q = Queue.Queue(maxsize = 10)
Queue.Queue类即是一个队列的同步实现。队列长度可为无限或者有限。
可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。

分为阻塞和非阻塞

Python Queue模块有三种队列及构造函数:
1、Python Queue模块的FIFO队列先进先出。   class queue.Queue(maxsize)
2、LIFO类似于堆，即先进后出。               class queue.LifoQueue(maxsize)
3、还有一种是优先级队列级别越低越先出来。        class queue.PriorityQueue(maxsize)

"""
import time,random
import queue,threading

q = queue.Queue()

def Producer(name):
  count = 0
  while count <10:
    print("制造包子ing")
    time.sleep(random.randrange(3))
    q.put(count)
    print('生产者 %s 生产了 %s 包子..' %(name, count))
    count +=1
    #q.task_done()
    #q.join()

def Consumer(name):
  count = 0
  while count <10:
    time.sleep(random.randrange(4))
    if not q.empty():
        data = q.get()
        #q.task_done()
        #q.join()
        print(data)
        print('消费者 %s 消费了 %s 包子...' %(name, data))
    else:
        print("包子吃完了")
    count +=1

c1 = threading.Thread(target=Producer, args=('小明',))
c2 = threading.Thread(target=Consumer, args=('小花',))
c3 = threading.Thread(target=Consumer, args=('小灰',))
c1.start()
c2.start()
c3.start()

c1.join()
c2.join()
c3.join()

print('结束')
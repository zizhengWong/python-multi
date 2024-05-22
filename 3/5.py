""" 
q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空，再执行别的操作

非阻塞版本
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
    q.task_done()
    #q.join()

def Consumer(name):
  count = 0
  while count <2:
    time.sleep(random.randrange(4))
    data = q.get()
    #q.task_done()
    print('等待中')
    q.join()
    print('消费者 %s 消费了 %s 包子...' %(name, data))
    count +=1

c1 = threading.Thread(target=Producer, args=('小明',))
c2 = threading.Thread(target=Consumer, args=('小花',))
c3 = threading.Thread(target=Consumer, args=('小灰',))
c4 = threading.Thread(target=Consumer, args=('小天',))

c1.start()
c2.start()
c3.start()
c4.start()
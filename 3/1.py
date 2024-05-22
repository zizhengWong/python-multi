""" 
同步：其他线程需要通过判断某个线程的状态来确定自己下一步的操作

每个线程都是独立运行且状态不可预测
初始情况下,Event对象中的信号标志被设置为假，如果有线程等待一个Event对象，
那么这个线程将会被一直阻塞直至该标志为真

学生线程的执行与否取决于老师线程
"""

""" 
1.模拟1个老师和10个学生，进行考试，我们需要的目的是学生线程要等待老师线程说完“大家现在考试”，然后学生线程去考试，
    之后老师线程说“考试结束”，学生线程放学回家，学生线程的执行与否取决于老师线程，所以这里用的Event
2.学生线程开始event.wait()，这个说明如果event如果一直不设置的话，学生线程就一直等待，等待一个event.set()操作
3.老师线程说完"大家现在要考试"，然后event.set()，执行event,设置完执行，
    学生线程就能够被唤醒继续执行下面的操作发出"啊啊啊啊啊啊"的叫苦连天
4.学生线程进行考试，并且执行event.clear()，清除event，因为他们在等老师说“考试结束”，
    之后他们在等老师线程的event.set()
5.老师线程执行event.set()，唤醒学生线程，然后下课回家.
"""
import threading
import time

class Teacher(threading.Thread):
    def run(self):
        print("大家现在要考试")
        print(event.isSet())
        event.set()
        time.sleep(3)
        print("考试结束")
        print(event.isSet())
        event.set()
class Student(threading.Thread):
    def run(self):
        event.wait()
        print("啊啊啊啊啊啊")
        time.sleep(1)
        event.clear()
        event.wait()
        print("下课回家")

if __name__=="__main__":
    event=threading.Event()
    threads=[]
    for i in range(10):
        threads.append(Student())
    threads.append(Teacher())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
"""
2.2.2 RLock
多重锁定是一个类似于 Lock 对象的同步原语，但同一个线程可以多次获取它。
这允许拥有锁定的线程执行嵌套的acquire() 和 release() 操作。

可以认为 RLock 包含一个锁定池和一个初始值为0的计数器，
每次成功调用 acquire()/release()，
计数器将+1/-1，为0时锁处于未锁定状态。
"""
import threading
import time

rlock = threading.RLock()
count = 0


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        if rlock.acquire():
            count += 1
            print('%s set count : %d' % (self.name, count))
            time.sleep(1)
            if rlock.acquire():
                count += 1
                print('%s set count : %d' % (self.name, count))
                time.sleep(1)
                rlock.release()
            rlock.release()


if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()

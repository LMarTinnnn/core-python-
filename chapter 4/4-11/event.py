"""
                    Condition object 的 通用版
-----------------------Event 对象的创建-------------

Event对象可以让任何数量的线程暂停和等待，event 对象对应一个 True 或 False 的状态（flag），刚创建的event对象的状态为False。
通过实例化Event类来获得一个event对象：
# e = threading.Event()
　　刚创建的event对象 e，它的状态为 False。


----------------------Event 对象的方法-------------

#e.clear()
　　将 e 的状态设置为 False。

　
# e.set()
　　将 e 的状态设置为 True。此时所有等待 e 的线程都被唤醒进入就绪状态。

# e.is_set()
　　返回 e 的 状态——True 或 False。

# e.wait(timeout=None)
　　如果 e 的状态为True，wait()立即返回True，否则线程会阻塞直到超时或者其他的线程调用了e.set()。
"""


import threading

cv = threading.Condition()
e = threading.Event()
alist = []


def producer():
    global alist
    for i in range(10):
        alist.append(i)
    e.set()


def consumer():
    e.wait()
    for i in alist:
        print(i)


if __name__ == '__main__':
    tproducer = threading.Thread(target=producer)
    tconsumer = threading.Thread(target=consumer)
    tconsumer.start()
    tproducer.start()

"""
实例方法：
acquire([timeout])/release()：调用关联的锁的相应方法。

wait([timeout])：调用这个方法将使线程进入 Condition 的等待池等待通知
并释放锁，直到另一个线程在条件变量上执行 notify() 或 notify_all() 方法将其唤醒为止。使用前线程必须已获得锁定，否则将抛出异常。


notify()：调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用 acquire() 尝试获得锁定（进入锁定池）；
其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。


notify_all()：唤醒所有等待此条件的线程。
"""
import threading

cv = threading.Condition()
alist = []


def producer():
    global alist
    cv.acquire()
    for i in range(10):
        alist.append(i)
    cv.notify()  # 唤醒等待cv的线程
    # notify() 不会立即解锁
    cv.release()


def consumer():
    cv.acquire()
    while not alist:  # 发现当前状态不对 调用wait方法 出让控制权 直到 notify() 
        cv.wait()
    cv.release()
    print(alist)
if __name__ == '__main__':
    tproducer = threading.Thread(target=producer)
    tconsumer = threading.Thread(target=consumer)
    tconsumer.start()
    tproducer.start()

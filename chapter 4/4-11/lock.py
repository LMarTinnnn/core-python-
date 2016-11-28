"""
原语锁定（互斥锁定）是一个同步原语，状态是“已锁定”或“未锁定”之一。
两个方法 acquire() 和 release() 用于修改锁定的状态。
如果有多个线程在等待获取锁定，当锁定释放时，只有一个线程能获得它。

构造方法：
Lock()：创建新的Lock对象，初始状态为未锁定。

实例方法：
Lock.acquire([timeout])：使线程进入同步阻塞状态，尝试获得锁定。 成功获取锁定返回 True，无法获取锁定返回False。
Lock.release()：释放锁。使用前线程必须已获得锁定，否则将抛出异常。
"""

"""
lock对象的方法

　　lock对象提供三种方法：acquire()、locked()和release()

# l.acquire(wait=True)
　　该函数需要结合参数 wait 进行讨论：

　　1. 当 wait 是 False 时，如果 l 没有上锁，那么acquire()调用将l上锁，然后返回True；

　　2. 当 wait 是 False 时，如果 l 已经上锁，那么acquire()调用对 l 没有影响，然后返回False；

　　3. 当 wait 是 True 时，如果 l 没有上锁，acquire()调用将其上锁，然后返回True；

　　4. 当 wait 是 True 时，如果 l 已经上锁，此时调用 l.acquire() 的线程将会阻塞，直到其他线程调用 l.release()，
    这里需要注意的是，就算这个线程是最后一个锁住 l 的线程，只要它以wait=True调用了acquire()，那它就会阻塞，因为Lock原语是不支持重入的。

　　可将，只要 l 没有上锁，调用 acquire()的结果是相同的。当l 上锁了，而 wait=False 时，线程会立即得到一个返回值，不会阻塞在等待锁上面；
    而 wait = True时，线程会阻塞等待其他的线程释放该锁，所以，一个锁上面可能有多个处于阻塞等待状态的线程。

# l.release()
　　解开 l 上的锁，要求：

    任何线程都可以解开一个已经锁上的Lock对象；
    l 此时必须处于上锁的状态，如果试图 release() 一个 unlocked 的锁，将抛出异常 thread.error。
    l一旦通过release()解开，之前等待它（调用过 l.acquire()）的所有线程中，只有一个会被立即被唤醒，然后获得这个锁。
"""


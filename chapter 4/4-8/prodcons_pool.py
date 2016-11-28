from concurrent.futures import ThreadPoolExecutor
from random import randint
from queue import Queue
from time import sleep


def writeQ(queue):
    print('Producing object for Q')
    queue.put('xxx')
    print('Q size now: ' + str(queue.qsize()))


def readQ(queue):
    queue.get()
    print('Consumed object from Q... \nQ size now: ' + str(queue.qsize()))


def writer(queue, loops_num):
    for i in range(loops_num):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops_num):
    for i in range(loops_num):
        readQ(queue)
        sleep(randint(2, 5))


def main():
    loops_num = randint(2, 5)
    q = Queue(32)

    n = randint(1, 5)
    with ThreadPoolExecutor(1) as executor:
        executor.submit(writer, q, loops_num)
        executor.submit(reader, q, loops_num)

    print('All Done!')

if __name__ == '__main__':
    main()
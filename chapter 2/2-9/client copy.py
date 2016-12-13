from socket import *
from time import ctime
import select, sys

BUFSIZ = 1024


def prompt():
    sys.stdout.flush()


def create_client():
    ADDR = ('', 1034)
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    prompt()
    try:
        while True:
            ready_read, ready_write, ready_exception = select.select([sys.stdin, client], [], [])
            for sock in ready_read:
                if sock == client:
                    data_got = client.recv(BUFSIZ)
                    if not data_got:
                        print('服务器坏掉啦啦啦啦啦啦～～～～')
                        sys.exit()
                    data_got = '[%s] %s' % (ctime(), data_got.decode())
                    # 这两个等效
                    #sys.stdout.write(data_got)
                    print(data_got.rstrip())
                    prompt()
                else:
                    data_to_send = '<%s:%s>: ' % client.getsockname() + sys.stdin.readline()
                    client.send(data_to_send.encode())
                    prompt()
    except:
        print('disconnected from chat room server')
        client.close()


if __name__ == '__main__':
    create_client()

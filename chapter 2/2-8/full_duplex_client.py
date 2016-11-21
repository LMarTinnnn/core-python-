from socket import *
from time import ctime
import select, sys

BUFSIZ = 1024


def create_client():
    ADDR = ('', 9991)
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    print('> ')
    while True:
        try:
            ready_read, ready_write, ready_exception = select.select([sys.stdin, client], [], [])
            for sock in ready_read:
                if sock == client:
                    data_got = client.recv(BUFSIZ)
                    if not data_got or data_got == b'Q\n':
                        sys.exit()
                    data_got = '[%s] %s' % (ctime(), data_got.decode())
                    sys.stdout.write(data_got)

                else:
                    data_to_send = sys.stdin.readline()
                    if not data_to_send or data_to_send == 'Q\n':
                        sys.exit()
                    client.send(data_to_send.encode())
        except:
            break
    print('disconnected from other socket')
    client.close()


if __name__ == '__main__':
    create_client()

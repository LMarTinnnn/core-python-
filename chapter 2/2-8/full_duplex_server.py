
# 全双工聊天
import socket, sys
import select
from time import ctime


def prompt():
    sys.stdout.flush()


def create_server(*, host='', port=9991):
    BUFSIZ = 1024
    ADDR = (host, port)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(ADDR)
    srv.listen(5)

    while True:
        print('waiting for connection')
        conn, add = srv.accept()
        print('connected from: ', str(add))
        print('> ')
        while True:
            try:
                ready_read, ready_write, ready_exception = select.select([sys.stdin, conn], [], [])
                for sock in ready_read:
                    if sock == conn:
                        data_got = conn.recv(BUFSIZ)
                        if not data_got or data_got == b'Q\n':
                            sys.exit()
                        data_got = '[%s] %s' % (ctime(), data_got.decode())
                        sys.stdout.write(data_got)
                    else:
                        data_to_send = sys.stdin.readline()
                        if not data_to_send or data_to_send == 'Q\n':
                            sys.exit()
                        conn.send(data_to_send.encode())
            except:
                break
        print('(%s) disconnected\n' % str(add))
        conn.close()
    srv.close()

if __name__ == '__main__':
    create_server()



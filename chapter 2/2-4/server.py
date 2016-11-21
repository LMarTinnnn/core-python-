# 更新tcp客户端。此处应该允许用户数指定主机名和端口号，且如果二者中的任何一个或者全部参数丢失，那么应当使用默认值

from time import ctime
import socket


def create_server(*, host='', port=9999):
    BUFSIZ = 1024
    ADDR = (host, port)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(ADDR)
    srv.listen(5)
    while True:
        print('waiting for connection')
        conn, addr = srv.accept()
        print('connected from: ', str(addr))
        while True:
            data = conn.recv(BUFSIZ)
            if not data:
                break
            data_tosend = b'[%s] %s' % (bytes(ctime(), 'utf-8'), data)
            conn.send(data_tosend)
        conn.close()
    srv.close()

if __name__ == '__main__':
    create_server()

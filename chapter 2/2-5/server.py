# 更新tcp客户端。此处应该允许用户数指定主机名和端口号，且如果二者中的任何一个或者全部参数丢失，那么应当使用默认值

from time import ctime
import socket
import os
import pickle
import re

_re_path = re.compile(r'ls (\w:([/\\].*)*)')


def create_server(*, host='', port=9999):
    BUFSIZ = 1024
    ADDR = (host, port)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(ADDR)
    srv.listen(5)
    while True:
        print('waiting for connection')
        conn, addr = srv.accept()
        print('connected from: \n', str(addr))

        while True:
            try:
                data = conn.recv(BUFSIZ)
            except:
                break
            if data == b'date':
                data_tosend = handler_date()
            elif data == b'os':
                data_tosend = handler_os()
            elif data == b'ls':
                data_tosend = handler_ls()
            elif _re_path.match(data.decode()):
                data_tosend = handler_ls(_re_path.match(data.decode()).group(1))
            else:
                data_tosend = 'illegal reuquest'
            try:
                conn.send(data_tosend.encode())
            except AttributeError:
                conn.send(data_tosend)

        conn.close()
    srv.close()


def handler_date():
    return ctime()


def handler_os():
    return os.name


def handler_ls(path=os.curdir):
    return pickle.dumps(os.listdir(path))

if __name__ == '__main__':
    create_server()



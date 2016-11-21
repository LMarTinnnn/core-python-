
# 半双工聊天
import socket
from time import ctime


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
            data_to_send = input('Message [Q to quit]:')
            if not data_to_send or data_to_send == 'Q':
                break
            data_to_send = '[%s] %s' % (ctime(), data_to_send)
            conn.send(data_to_send.encode())
            print('Wait for information...')
            data_got = conn.recv(BUFSIZ)
            if not data_got or data_got == b'Q':
                break
            data_to_show = data_got.decode()
            print(data_to_show)
        conn.close()
        print('Connection break')
    srv.close()

if __name__ == '__main__':
    create_server()

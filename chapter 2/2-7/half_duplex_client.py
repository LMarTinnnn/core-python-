from socket import *
from time import ctime

def create_client(host='', port=9999):
    ADDR = ('127.0.0.1', 9999)
    cli = socket(AF_INET, SOCK_STREAM)
    cli.connect(ADDR)
    print('Connection made.')
    while True:
        data_to_send = input('Message [Q to quit]:')
        if not data_to_send or data_to_send == 'Q':
            break
        data_to_send = '[%s] %s' % (ctime(), data_to_send)
        print('Wait for information...')
        data_got = cli.recv(1024)
        if not data_got or data_got == b'Q':
            break
        print(data_got.decode())


        cli.send(data_to_send.encode())
    print('Connection break')
    cli.close()


if __name__ == '__main__':
    create_client()

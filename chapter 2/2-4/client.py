from socket import *


def create_client(host='localhost', port=9999):
    ADDR = (host, port)
    BUFFSIZ = 1024
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    while True:
        data = input('> ')
        if not data:
            break
        client.send(data.encode())
        data = client.recv(BUFFSIZ)
        if not data:
            break
        print(data.decode())
    client.close()

if __name__ == '__main__':
    create_client()
import socket
import time
import random


def client_maker(current_address, msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(current_address)
        client.send((msg+'\n').encode())
        response = client.recv(1024).decode()
        print('Received: {}'.format(response))


if __name__ == '__main__':
    while True:
        time.sleep(random.randrange(0, 4))
        client_maker(('', 9998), 'Hello, World1')

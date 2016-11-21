import socket
import time
import random


def client_maker(current_address):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(current_address)
        while True:
            msg = input('Input msg ([Q] for quit) : ')
            if msg == 'Q':
                break
            client.send((msg+'\n').encode())
            response = client.recv(1024).decode()
            if not response:
                break
            print('Received: {}'.format(response))
        print('Connection broke')


if __name__ == '__main__':
    while True:
        client_maker(('', 9992))

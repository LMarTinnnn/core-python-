from socket import *
import pickle

menu = {
        'os': 'show os name',
        'date': 'show current time',
        'ls': 'list all dir in current dir'
}


def create_client(host='goalsocket', goalport=9999):
    ADDR = (host, goalport)
    BUFFSIZ = 1024
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    while True:
        show_info = ['[%s] %s' % (opt, desc) for opt, desc in menu.items()]
        show_info = '\n'.join(show_info)
        print(show_info)
        data = input('Enter choice: ')
        if not data:
            break
        client.send(data.encode())
        data = client.recv(BUFFSIZ)
        if not data:
            break
        try:
            print(data.decode(), '\n')
        except UnicodeDecodeError:
            print(pickle.loads(data), '\n')
    client.close()

if __name__ == '__main__':
    create_client()

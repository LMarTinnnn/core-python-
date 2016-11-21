import socket

if __name__ == '__main__':

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Try connecting')
    client.connect(('', 1123))
    welcome = client.recv(1024)
    print(welcome.decode())
    client.send(b'@#')
    info = client.recv(1024)
    print(info.decode())
    while True:
        data = input('Key word([Q] for quit): ')
        if data == 'Q':
            break
        client.send(data.encode())
        data_got = client.recv(1024)
        if not data_got:
            print('Server GG')
            break
        print(data_got.decode())

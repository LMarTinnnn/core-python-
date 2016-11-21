import socket
from time import ctime
import sys
import pickle
import select

class NameServer(object):

    def __init__(self, port, data_path):
        self.port = port
        self.data_path = data_path
        self.srv = self.create_socket()
        self.data = self.load_data()
        self.descriptors = [self.srv, sys.stdin]

    def create_socket(self):
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.bind(('', self.port))
        srv.listen(10)
        print('Server listening at %s ...' % self.port)
        return srv

    def load_data(self):
        try:
            with open(self.data_path, 'rb') as f:
                data = pickle.load(f)
        except:
            data = {}
        return data

    def accept_conn(self):
        conn, addr = self.srv.accept()
        conn.send(b'Welcome to name server')
        self.descriptors.append(conn)
        print('Connection from %s:%s' % addr)

    def add_data_online(self, host, port, key_word):
        self.data[key_word] = [(host, port), 0]

    def add_data_offline(self):
        try:
            while True:
                host = input('HOST: ')
                port = int(input('Port: '))
                key_word = input('key_word: ')
                self.data[key_word] = [(host, port), 0]
                check = input('[Q] for quit: ')
                if check == 'Q':
                    break
        finally:
            self.save_data()
            self.srv.close()

    def del_data_offline(self):
        try:
            while True:
                    try:
                        key = input('The key you want to delete: ')
                        self.data.pop(key)
                        check = input('Q for quit: ')
                        if check == 'Q':
                            break
                    except:
                        print('No that key_word')
                        raise
        finally:
            self.save_data()
            self.srv.close()

    def save_data(self):
        with open(self.data_path, 'wb') as f:
            pickle.dump(self.data, f)

    def handle_request(self, key_word, connection_socket):
        try:
            response = self.data[key_word][0]
            self.data[key_word][1] += 1

            connection_socket.send(str(response).encode())
        except KeyError:
            connection_socket.send(b'No such file')

    def check_live(self):
        pass

    def show_data_srv(self):
        show_info = []
        for net in self.data.items():
            show_info.append(str(net[0]) + ': ' + str(net[1][0]) + ' Ping Times: ' + str(net[1][1]))
        msg = '\n'.join(show_info)
        print(msg)

    def show_data_client(self, conn):
        show_info = []
        for net in self.data.items():
            show_info.append(str(net[0]) + ': Ping Times: ' + str(net[1][1]))
        msg = '\n'.join(show_info)
        conn.send(msg.encode())

    def run(self):
        try:
            while True:
                ready_read, ready_write, ready_exception = select.select(self.descriptors, [], [])
                for sock in ready_read:
                    if sock == self.srv:
                        self.accept_conn()
                    elif sock == sys.stdin:
                        data = (sys.stdin.readline()).rstrip()
                        if data == '@#':
                            self.show_data_srv()
                    else:
                        try:
                            request = sock.recv(1024)
                            key_word = (request.decode()).rstrip()
                            if not request:
                                print('[%s:%s] had already left' % sock.getpeername())
                                sock.close()
                                self.descriptors.remove(sock)
                                break
                            if key_word == '@#':
                                self.show_data_client(sock)
                            else:
                                self.handle_request(key_word, sock)
                        except:
                            sock.close()
                            self.descriptors.remove(sock)
                            raise
        except:
            print('Something bad happened')
            raise
        finally:
            print('Emergency saving')
            self.save_data()
            self.srv.close()


if __name__ == '__main__':
    NM = NameServer(1123, 'name_server_data.txt')
    #NM.add_data_offline()
    NM.show_data_srv()
    #NM.del_data_offline()
    NM.run()

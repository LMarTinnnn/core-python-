import socket, sys
import select
import re

_re_msg = re.compile(r'<[\d.:]*>: (@[#$%])')


class ChatServer(object):
    def __init__(self, port):
        self.port = port
        self.srv = self.create_socket()
        self.descriptor = [self.srv, sys.stdin]

    def create_socket(self,):
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.bind(('', self.port))
        srv.listen(10)
        print('Waiting for connection')
        return srv

    def accept_new_connection(self):
        conn, remaddr = self.srv.accept()
        self.descriptor.append(conn)
        msg_wel = 'Welcome to chat room [%s]' % self.port
        conn.send(msg_wel.encode())
        msg_join = ('<%s:%s> 进入房间' % remaddr + str(self.port))
        print(msg_join)
        self.broadcast(conn, msg_join.encode())

    def broadcast(self, msg_sender, msg_bytes):
        for sock in self.descriptor:
            if sock != self.srv and sock != msg_sender and sock != sys.stdin:
                sock.send(msg_bytes)

    def system_operation(self, sock, operation):
        if operation == '@#':
            num = len(self.descriptor) - 2
            msg_num = 'There are %s people in the chat room \n' % num
            sock.send(msg_num.encode())

    def run(self):
        try:
            while True:
                rearead, reawrite, reaexception = select.select(self.descriptor, [], [])
                for s in rearead:
                    if s == self.srv:
                        self.accept_new_connection()
                    elif s == sys.stdin:
                        msg_send = '来自管理员：' + sys.stdin.readline()
                        self.broadcast(self.srv, msg_send.encode())
                    else:
                        msg_got = s.recv(1024)
                        if not msg_got:
                            addr = s.getpeername()
                            msg_left = '<%s:%s> left the chat room\r\n' % addr
                            print(msg_left.rstrip())
                            s.close()
                            self.descriptor.remove(s)
                            self.broadcast(self.srv, msg_left.encode())
                        elif _re_msg.match((msg_got.decode()).rstrip()):
                            self.system_operation(s, _re_msg.match((msg_got.decode()).rstrip()).group(1))
                        else:
                            self.broadcast(s, msg_got)
        except:
            print('something bad happened')
        finally:
            print('Emergency socket closing')
            self.srv.close()

if __name__ == '__main__':
    c1 = ChatServer(1034)
    c1.run()


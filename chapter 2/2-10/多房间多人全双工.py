import socket, sys
import select
import re
import threading
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
        msg_wel = 'Welcom to chat room [%s]' % self.port
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

c1 = ChatServer(12333)
c2 = ChatServer(12222)
t1 = threading.Thread(target=c1.run)
t2 = threading.Thread(target=c2.run)
t1.start()
t2.start()
t1.join()
t2.join()
# ----- 不太方便管理员发信息 还是要调整一下

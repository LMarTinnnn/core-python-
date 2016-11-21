from socket import *
import select
import sys


def create_server(*, host='', port=9979):

    def broadcast(sock_send_msg, sock_list, msg_in):
        for s in sock_list:
            if s == sock_send_msg or s == srv:
                pass
            else:
                try:
                    s.send(msg_in)
                except :
                    s.close()
                    sock_list.remove(s)

    ADDR = (host, port)
    srv = socket(AF_INET, SOCK_STREAM)
    srv.bind(ADDR)
    srv.listen(10)
    connection_list = [srv]
    addr_dic = {}
    print('Char room open')
    try:
        while True:
            ready_read, ready_write, ready_exception = select.select(connection_list + [sys.stdin], [], [])
            for sock in ready_read:
                if sock == srv:
                    conn, addr = srv.accept()
                    conn.send(b'Welcome\n')
                    addr_dic[conn] = addr
                    connection_list.append(conn)
                    print('<%s:%s> 进入房间' % addr)
                    broadcast(conn, connection_list, ('<%s:%s> 进入房间\n' % addr).encode())

                elif isinstance(sock, socket):
                    try:
                        msg = sock.recv(1025)
                        if not msg:
                            sock.close()
                            connection_list.remove(sock)
                            print(str(addr_dic[sock]) + 'left the room')
                            sys.stdout.flush()
                            leave_msg = ('--------' + str(addr_dic[sock]) + 'left the room\n').encode()
                            broadcast(sock, connection_list, leave_msg)
                        else:
                            broadcast(sock, connection_list, msg)
                    except:
                        continue
                        
                else:
                    msg = sys.stdin.readline()
                    broadcast(srv, connection_list, msg.encode())
    except:
        srv.close()

create_server()

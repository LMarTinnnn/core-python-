import socket
import threading
import socketserver
from time import ctime


class ThreadTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadTCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        thread_info = threading.current_thread().name.encode()
        t_bytes = ('[%s] ' % ctime()).encode()
        self.wfile.write(t_bytes + thread_info + b'  ' + self.data)


if __name__ == '__main__':
    ADDR = ('', 9998)
    srv = ThreadTCPServer(ADDR, ThreadTCPRequestHandler)
    print('ready to serve')
    srv.serve_forever()
    '''主线程不必用threading'''
    #main_Thread = threading.Thread(target=srv.serve_forever)
    #print('Thread will start')
    #main_Thread.start()
    #print("server loop running in thread", main_Thread.name)


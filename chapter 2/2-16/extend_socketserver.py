import socket
import threading
import socketserver
from time import ctime


class ThreadTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadTCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('Connection from %s:%s' % self.client_address)
        while True:
            self.data = self.rfile.readline().strip()
            if not self.data:
                break
            thread_info = threading.current_thread().name.encode()
            t_bytes = ('[%s] ' % ctime()).encode()
            try:
                self.wfile.write(t_bytes + thread_info + b'  ' + self.data)
            except BrokenPipeError:
                break
        print('%s:%s left' % self.client_address)


if __name__ == '__main__':
    ADDR = ('', 9992)
    srv = ThreadTCPServer(ADDR, ThreadTCPRequestHandler)
    print('ready to serve')
    srv.serve_forever()


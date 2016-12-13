from http.server import HTTPServer, CGIHTTPRequestHandler


def main():
    srv = HTTPServer(('', 8000), CGIHTTPRequestHandler)
    try:
        print('Press ^c to stop the server machine.')
        srv.serve_forever()
    except KeyboardInterrupt:
        print('Shunting down...')
        srv.socket.close()

if __name__ == '__main__':
    main()

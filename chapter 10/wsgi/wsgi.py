from wsgiref.simple_server import make_server
from app import app

srv = make_server('', 8000, app)

if __name__ == '__main__':
    srv.serve_forever()

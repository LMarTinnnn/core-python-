import socket

host = 'www.qq.com'
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(host), port))

client.sendall(b'GET / HTTP/1.1\r\nHost: www.qq.com\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    data = client.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
data = b''.join(buffer)
client.close()

header, html = data.split(b'\r\n\r\n', 1)
with open('tencent.html', 'wb') as file:
    file.write(html)
with open('tencent.txt', 'wb') as h:
    h.write(header)


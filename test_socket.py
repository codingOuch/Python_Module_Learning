#!/usr/bin/env python
# -*-coding: utf-8 -*-

import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set up connection
s.connect(('www.bing.com', 80))

# send data
s.send(b'GET / HTTP/1.1\r\nHost: www.bing.com\r\nConnection: close\r\n\r\n')

# receive data
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# close connection
s.close()

print(data)

header, html = data.split(b'\r\n\r\n', 1)
print(header)
with open('baidu.html', 'wb') as f:
    f.write(html)

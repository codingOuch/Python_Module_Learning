#!/usr/bin/env python
# -*-coding: utf-8 -*-

import socket
import threading


# new thread tcplink
def tcplink(sock, addr):
    welcome_info = bytes(f'Welcome aboard, {addr[0]}: {addr[1]}', encoding='utf-8')
    sock.send(welcome_info)
    while 1:
        data = sock.recv(1024)
        print(type(data))
        sock.send(bytes(f'You entered: {data}', encoding='utf-8'))


# create a new socket by tcp
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to localhost:8888
server_sock.bind(('127.0.0.1', 8888))
server_sock.listen(5)
print('Waiting for connection...')

while True:
    sock, addr = server_sock.accept()
    print(f'New user from {addr[0]}: {addr[1]}')
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


#!/usr/bin/env python
# -*-coding: utf-8 -*-

import socket

# create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set up welcome
s.connect(('127.0.0.1', 8888))

# receive welcome info
while 1:
    send_data = bytes(input('Enter your message:'), encoding='utf-8')
    s.send(send_data)
    recv_data = s.recv(1024)
    print(recv_data)

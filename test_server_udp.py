#!/usr/bin/env python
# -*-coding: utf-8 -*-

import socket

# create a new socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket to addr
host = '127.0.0.1'
port = 9999
s.bind((host, port))
print('Build UDP socket on %s: %s' % (host, port))
# get data from any client
data, addr = s.recvfrom(1024)
print('Received from %s: %s' % addr)
while True:
    s.sendto(b'Welcome abo')

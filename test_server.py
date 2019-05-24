#!/usr/bin/env python
# -*-coding: utf-8 -*-

import socket
import threading


def tcplink():
    print()


# CREATE NEW SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# LISTEN PORT
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
while True:
    # receive a new connection
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


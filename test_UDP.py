#!/usr/bin/env python
# *_*coding:utf-8 *_*
"""
    @Author:    Howard Zhu
    @Date:      2019-5-25
    @File:      test_UDP.py
    @Software:  PyCharm 
"""

import socket
import threading


def udplink(sock, data, addr):
    print(f'Welcome aboard, {addr[0]}: {addr[1]}')
    sock.sendto(bytes(f'You entered: {data}', encoding='utf-8'), addr)

# create the new socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the port
s.bind(('127.0.0.1', 9999))

print('Bind UDP on port 9999...')
while True:
    data, addr = s.recvfrom(1024)
    t = threading.Thread(target=udplink, args=(s, data, addr))
    t.start()

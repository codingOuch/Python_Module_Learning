#!/usr/bin/env python
# *_*coding:utf-8 *_*
"""
    @Author:    Howard Zhu
    @Date:      2019-5-27
    @File:      test_udp_client.py
    @Software:  PyCharm 
"""
import socket

# Const
HOST = '127.0.0.1'
PORT = 9999

# create a new socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send the message
while True:
    send_data = bytes(input('Enter your message: '), encoding='utf-8')
    client_sock.sendto(send_data, (HOST, PORT))
    recv_data = client_sock.recv(1024)
    print(recv_data)

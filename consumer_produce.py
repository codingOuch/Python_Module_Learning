#!/usr/bin/env python
# *_*coding:utf-8 *_*
"""
    @Author:    Howard Zhu
    @Date:      2019-6-2
    @File:      consumer_produce.py
    @Software:  PyCharm 
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)

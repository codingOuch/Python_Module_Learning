#!/usr/bin/env python
# -*-coding: utf-8 -*-


def generator_1():
    total = 0
    while True:
        x = yield
        print(f'+ {x}')
        if not x:
            break
        total += x
    return total

# def generator_1():
#     total = 0
#     while True:
#         x = yield
#         print('加',x)
#         if not x:
#             break
#         total += x
#     return total


def generator_2():
    while 1:
        total = yield from generator_1()
        print(f'Total: {total}')


def averager():
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield averager
        total += term
        count += 1
        das = total / count
        print(f'average: {averager}')

if __name__ == '__main__':
    # g1 = generator_1()
    # next(g1)
    # g1.send(1)
    # g1.send(2)
    # g1.close()
    # g2 = generator_2()
    # next(g2)
    # g2.send(1)
    # g2.send(2)
    # g2.send(None)
    #
    av = averager()
    next(av)
    av.send(10.0)
    av.send(30.0)
    av.send(5.0)

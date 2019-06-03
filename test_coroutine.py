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


if __name__ == '__main__':
    g1 = generator_1()
    next(g1)
    g1.send(1)
    g1.send(2)
    g1.close()
    g2 = generator_2()
    next(g2)
    g2.send(1)
    g2.send(2)
    g2.send(None)


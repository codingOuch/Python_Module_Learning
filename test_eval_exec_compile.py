#!/usr/bin/env python
# -*-coding: utf-8 -*-

x = 10
y = 3

expr = '''
x = 1
y = 2
z = x + y
print(z)
'''

expr_eval = '10+20'

def test_eval():
    a = eval('x+y', {'x': 1, 'y': 2}, {'y': 4})
    print(a)

    b = eval('x+y')
    print(b)

    c = eval('print(x, y)')
    print(c)


def test_exec():
    a = exec('print(x+y)', {'x': 1, 'y': 2}, {'y': 4})
    print(a)

    b = exec('print(x+y)')
    print(b)

    c = exec('print(x, y)')
    print(c)


def test_compile():
    code_expr = compile(expr_eval, '<strindasd>', 'eval')
    a = eval(code_expr)
    print(a)


# test_eval()
# test_exec()
test_compile()

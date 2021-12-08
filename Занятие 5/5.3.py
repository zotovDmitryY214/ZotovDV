# -- coding: utf-8 --
def f():
    s = int(input())
    a = 2
    b = 1
    while a <= s:
        a *= 2
        b += 1
    print( b - 1,  a // 2)
f()



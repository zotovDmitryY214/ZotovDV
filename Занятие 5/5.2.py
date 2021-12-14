# -- coding: utf-8 --
def f():
    a = 2
    print("Введите число не меньше 2")
    n = int(input())
    while n % a != 0:
        a += 1
    print(a)
f()



# -- coding: utf-8 --
def f():
    print("Введите сколько км спортсмен пробежал в первый день")
    x = int(input())
    print("Введите число")
    y = int(input())
    counter = 1
    while x < y:
        x *= 1.1
        counter += 1
    print(counter)
f()



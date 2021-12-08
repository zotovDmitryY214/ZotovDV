"# -- coding: utf-8 --"
def f():
    print("Введите кол-во минут")
    n = int(input())
    h = n // 60
    min = n % 60
    if h >= 24:
        h %= 24
    return str(h) + " : " + str(min)
print("На часах ",f())
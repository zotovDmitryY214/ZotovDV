# -- coding: utf-8 --
def f():
    print("Введите строку")
    s = str(input())
    a = len(s) // 2 + len(s) % 2
    b = (s[a:] + s[:a])
    return b
print(f())



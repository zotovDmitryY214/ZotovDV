"# -- coding: utf-8 --"
def f():
    print("Введите первый катет")
    a = int(input())
    print("Введите второй катет")
    b = int(input())
    return (0.5 * a * b)
print("Площадь треугольника равна ", f())
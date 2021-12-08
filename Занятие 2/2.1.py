"# -- coding: utf-8 --"
def sum():
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    print("Введите третье число")
    c = int(input())
    return str(a + b + c)
print("Сумма равна ", sum())
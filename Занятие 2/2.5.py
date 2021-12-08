"# -- coding: utf-8 --"
def f():
   print("Введите первое число")
   a = int(input())
   print("Введите второе число")
   b = int(input())
   print("Введите третье число")
   c = int(input())
   return min(a,b,c)
print("Минимальное число из введённых - ",f())
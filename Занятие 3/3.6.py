"# -- coding: utf-8 --"
def f():
   print("Введите число n")
   n = int(input())
   a = 1
   for i in range(1, n + 1):
       a *= i
   return a
print(f())
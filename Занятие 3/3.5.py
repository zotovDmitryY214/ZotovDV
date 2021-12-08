"# -- coding: utf-8 --"
def f():
   print("Введите число n")
   n = int(input())
   s = 0
   for i in range(1, n + 1):
       s += i ** 3
   return s
print(f())
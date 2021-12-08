"# -- coding: utf-8 --"
def f():
   print("Введите число n")
   n = int(input())
   s = 0
   p = 1
   for i in range(1, n + 1):
       p *= i
       s += p
   return s
print(f())
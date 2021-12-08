# -- coding: utf-8 --
def f():
   print("Введите число А")
   A = int(input())
   print("Введите число В")
   B = int(input())
   for i in range(A, B - 1, -1):
       if i % 2 != 0:
           print(i)
   return "End"
print(f())

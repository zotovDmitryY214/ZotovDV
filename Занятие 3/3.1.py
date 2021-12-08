# -- coding: utf-8 --
def f():
   print("Введите число А")
   A = int(input())
   print("Введите число В")
   B = int(input())
   if A > B:
       print("Введите числа корректно")
   for i in range(A, B + 1):
       print(i)
   return "End"
print(f())

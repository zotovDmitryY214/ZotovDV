"# -- coding: utf-8 --"
def f():
   print("Введите n")
   n = int(input())
   print("Введите m")
   m = int(input())
   print("Введите k")
   k = int(input())
   if n * m > k and (k % m == 0 or k % n == 0):
       return "Da"
   else:
       return "Net"
print(f())
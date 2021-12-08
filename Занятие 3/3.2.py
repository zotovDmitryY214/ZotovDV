# -- coding: utf-8 --
def f():
   print("Введите число А")
   A = int(input())
   print("Введите число В")
   B = int(input())
   if A < B:
       for i in range(A, B + 1):
           print(A)
           A += 1
   else:
       for i in range(B, A + 1):
           print(A)
           A -= 1
   return "End"
print(f())

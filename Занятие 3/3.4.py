# -- coding: utf-8 --
n = int(input())
s = 0
def f(n,s):
   for i in range(n):
       s += int(input())
   print(s)
   return "End"
print(f(n,s))

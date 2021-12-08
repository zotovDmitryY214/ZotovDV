"# -- coding: utf-8 --"
def f():
   count = 0
   print("Введите первое число")
   a = int(input())
   print("Введите второе число")
   b = int(input())
   print("Введите третье число")
   c = int(input())
   if a == b:
       count += 1
   if a == c:
       count += 1
   if b == c:
       count += 1
   if count == 1:
       return count * 2
   else:
       return count
print(f())
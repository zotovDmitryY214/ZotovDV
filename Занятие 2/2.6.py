# -- coding: utf-8 --
def f():
   print("Введите номер столбца первой клетки(1-8)")
   x1 = int(input())
   print("Введите номер строки первой клетки(1-8)")
   y1 = int(input())
   print("Введите номер столбца второй клетки(1-8)")
   x2 = int(input())
   print("Введите номер строки второй клетки(1-8)")
   y2 = int(input())
   if x1 % 2 == x2 % 2:
       if y1 % 2 == y2 % 2:
           return "Da"
       else:
           return "Net"
   else:
       if y1 % 2 != y2 % 2:
           return "Da"
       else:
           return "Net"
print(f())

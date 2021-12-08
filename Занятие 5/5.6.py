"# -- coding: utf-8 --"
n = int(input())
a = 0
while n != 0:
    k = int(input())
    if k != 0 and n < k:
        a += 1
    n = k
print(a)


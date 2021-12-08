# -- coding: utf-8 --
s = input()
def f(s):
	a = (s[len(s) // 2:] + s[:len(s) // 2])
	print(a)
f(s)



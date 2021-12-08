"# -- coding: utf-8 --"
s = input()
def f(s):
	s = s[:s.find('h')] + s[s.rfind('h') + 1:]
	print(s)
f(s)



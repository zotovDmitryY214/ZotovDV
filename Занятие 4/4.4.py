"# -- coding: utf-8 --"
s = input()
def f(s):
    w1 = s[:s.find(' ')]
    w2 = s[s.find(' ') + 1:]
    print(w2 + ' ' + w1)
f(s)



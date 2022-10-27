s = 'welcome to python'
print(s.split())

s2 = '2018.8.15'
print(s2.split('.'))

s3 = 'hello,world!'
print(s3.split(','))

s4 = 'welcome, to, python, and , bla, bla   '
print([x.strip() for x in s4.split(',')])

s5 = 'welcome, to, python, and , bla, bla   '
print(s4.split(', '))
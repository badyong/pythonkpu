s = 'Hello, world'
print(s.lower())
print(s.upper())

s2 = '       hello,world!       '
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())

s3 = '#######this is an example#####'
print(s3.strip('#'))
print(s3.lstrip('#'))
print(s3.lstrip('#'))
print(s3.strip('#').capitalize())
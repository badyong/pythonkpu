import random 
import string
n_digits = int(input('몇 자리의 비밀번호를 원하십니까:'))
number = '123456789'
pw = string.ascii_letters+number
otp =''
for i in range(n_digits):
    otp += random.choice(pw)
print(otp)
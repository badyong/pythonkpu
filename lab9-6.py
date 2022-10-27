import re
txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'
output = re.findall('\S+@[a-z.]+',txt)
id = re.findall('[a-z]+[a-z]+[a-z]',txt)
print(output)
print(id)


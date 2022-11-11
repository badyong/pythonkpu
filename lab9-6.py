import re
txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'
output = re.findall('\S+@[a-z.]+',txt)
id = re.findall('\S+@',txt)
id = ''.join(id)
id = id.split('@')
id = [x for x in id if x != ""]
print(output)
print(id)


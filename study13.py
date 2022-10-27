import string

src_str = string.ascii_uppercase
dst_str = src_str[3:]+src_str[:3]
print(dst_str)
b = input("입력하세요:") # 내가 D를 입력하면 3이 들어감

for ch in b:
    if ch in src_str:
        print("응맞아")



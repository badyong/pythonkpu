st = input("단어를 입력하세요:")
bl = ['a','e','i','o','u',]
for ch in st:
    if ch in bl:
        break
    print(ch,end='')    
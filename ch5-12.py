st = input("단어를 입력하세요:")
for ch in st:
    if ch in ['a','e','i','o','u', 'A','E','I','O','U']:
        break
    print(ch, end='')
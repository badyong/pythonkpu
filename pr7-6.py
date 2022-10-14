a = [int(x) for x in input("정수를 입력하세요").split()]
print(a)
a2 = [int(x) for x in input("정수를 입력하세요").split() if x.isdigit()]
print(a2)
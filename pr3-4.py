num = int(input("정수를 입력하세요"))
if num >0:
    if num & 2==0:
        print('짝수입니다')
    else:
        print('홀수입니다')
else:
    print("음의 정수를 입력하셨습니다 ")

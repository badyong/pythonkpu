num = int(input("정수를 입력하세요"))
if num >= 0:
    print("양수입니다")
    if num == 0:
        print("0입니다")
    elif num % 2 ==0:
        print("짝수입니다")
    else:
        print("홀수입니다")
else:
    print("음의 정수를 입력하셨스2니다")
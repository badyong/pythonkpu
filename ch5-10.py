import random
tries = 0
guess = 0
answer =random.randint(1,100)
print("정답은",answer)
print("1부터 100까재의 숫자를 맞추시오 총 10번의 기회가 있습니다")
while tries < 10:
    guess = int(input("숫자를 입력하세요"))
    tries = tries + 1
    if guess < answer :
        print("낮음")
    if guess > answer:
        print("높음")
    if guess == answer :
        print("정답을 맞추셨습니다 총 시도 횟수 =",tries)
        break    
print("종료합니다")
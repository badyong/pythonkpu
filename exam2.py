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
    if guess == answer:
        print("축하합니다 정답은",answer,"입니다",end="")
        break

print()
print("프로그램이 종료되었습니다")
import random 
n = random.randint(1,3)
if n == 1:
    computer = "왼쪽"
if n ==2:
    computer = "중앙"
else:
    computer = "오른쪽"
user = input("어디를 공격하시겠어요?(왼쪽,중앙,오른쪽): ")
if computer == user:
    print("공격에 실패하셨습니다")
else:
    print("축하합니다 !! 공격에 성공하였습니다.")
print("컴퓨터 수비위치:",computer)
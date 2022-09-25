import random
dice1 =random.randint(1,6)
dice2 =random.randint(1,6)
player1 = input("Player1의 이름:")
player2 = input("Player2의 이름:")
print("----주사위를 굴립니다----")
print(player1,"의 주사위 번호는",dice1)
print(player2,"의 주사위 번호는",dice2)
if dice1 > dice2:
    print(player1,"이 이겼습니다")
elif dice1 < dice2:
    print(player2,"이 이겼습니다")
else:
    print("비겼습니다")
import random
while True:
    x = random.randint(1,100)
    y = random.randint(1,100)
    print(x,'-',y,'=',end = '')
    answer = int(input())
    if answer == x-y:
        print("잘했어요")
    else:
        print("정답은",x-y,"입니다 다음엔 잘할수있죠?")
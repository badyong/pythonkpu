total = 0 
answer = "yes"
while answer == "yes":
    number = int(input("숫자를 입력하세요"))
    total = total + number
    answer = input("계속 하시겠습니까 yes or no")
print("합계는 ",total)
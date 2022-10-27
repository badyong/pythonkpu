money = int(input("지불한 돈의 가격을 입력하세요:"))
price = int(input("물건의 가격을 입력하세요:"))
change = money-price
print("거스름돈",change)
change500 = change //500
change = change % 500
chagne100 = change //100
change = change % 100 
change10 = change //10
print("500원 동전의 개수:",change500)
print("100원의 동전의 개수:",chagne100)
print("10원의 동전의 개수:",change10)
money = int(input("투입한 돈:"))
price = int(input("물건값:"))
change = money-price
print("거스름돈:",change)
coins500 = change // 500
change = change % 500
coins100 = change // 100
print("500원 동전의 개수:",coins500)
print("100원 동전의 개수:",coins100)
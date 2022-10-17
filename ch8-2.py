items = {"커피음료":7,"펜":3,"종이컵":2,"우유":1,"콜라":4,"책":5}
while True:
    choice = int(input("메뉴를 선택하시오1) 재고조회 2) 입고 3) 출고 4) 종료"))
    if choice == 1:
        name = input("물건의 이름을 입력하시오:")
        print("재고",items[name])
    elif choice == 2:
        name,num = input("입고를 할 물건의 이름과 수량을 입력하시오:").split(' ')
        items[name] = items[name]+int(num)
        print(name,'의 재고',items[name])
    elif choice == 3:
        name,num = input("출고를 할 물건의 이름과 수량을 입력하시오:").split(' ')
        if int(num) > items[name]:
            print("물건의 갯수를 다시 확인해주세요")
        else:
            items[name] = items[name]-int(num)
            print(name, '의 재고', items[name])
    elif choice == 4:
        print("프로그램을 종료합니다")
        break

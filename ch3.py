time = int(input("초를 입력하세요"))
hour = time/3600
min = (time/60)%60
sec = time%60
print("입력한 시간은 :",int(hour),"시간",int(min),"분",int(sec),"초 입니다")
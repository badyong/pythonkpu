import matplotlib.pyplot as plt
x = [x for x in range(20)]         #0에서 20까지의 정수 x
y = [x ** 2 for x in range(20)]    #0에서 20까지의 정수 x에 대한 x ** 2
z = [x ** 3 for x in range(20)]    #0에서 20까지의 정수 x에 대한 x ** 3
q = [2 ** t for t in x]
plt.plot(x, x, label = 'linear')   #각 선에 대한 레이블(설명)
plt.plot(x, y, label = 'quadratic')
plt.plot(x, z, label = 'cubic')
plt.plot(x, q, label = 'power')
plt.xlabel('x label')         #x축 라벨 
plt.ylabel('y label')         #y축 라벨 
plt.title('My plot')            #차트 제목
plt.legend()                  #디폴트 위치에 범례 생성 
plt.show()
 

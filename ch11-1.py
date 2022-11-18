import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(1000)
y = (3-(-3))*np.random.rand(1000)+-3 #3과 -3 사이 난수생성하기위해서
plt.plot(x,y,color = 'red', marker='o')
plt.title('numbers')
plt.show()
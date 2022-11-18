import math
import matplotlib.pyplot as plt
x = []
y = []
x2 = []
y2 = []
for angle in range(360):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))
for angle in range(360):
    x2.append(angle)
    y2.append(math.cos(math.radians(angle)))

plt.plot(x,y)
plt.plot(x2,y2)
plt.title("cos,sin,wave")
plt.show()
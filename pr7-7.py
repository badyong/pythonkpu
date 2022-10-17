xy = [(x,y) for x in [1,2,3] for y in [3,1,4]]
print(xy)
xy2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(xy2)
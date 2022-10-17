population = ["Seoul",9765,"Busan",3441,"Incheon",2954]
print('서울인구:',population[1])
print('인천인구:',population[-1])

cities = population[0::2]
print('도시 리스트:',cities)
pops = population[1::2]
print('인구의 합:',sum(pops))
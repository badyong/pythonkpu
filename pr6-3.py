def calc(n1,n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2
    
n1, n2 =200 , 100
t1,t2,t3,t4 = calc(n1,n2)
print(n1,'+',n2,'=',t1)
print(n1,'-',n2,'=',t2)
print(n1,'*',n2,'=',t3)
print(n1,'/',n2,'=',t4)
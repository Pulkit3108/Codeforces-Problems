import math
n,h=map(int,input().split())
for i in range(1,n):
    x=math.sqrt(i/n)*h
    print(x,end=' ')

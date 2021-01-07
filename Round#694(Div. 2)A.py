import math
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    c1=sum(a)
    c1=math.ceil(c1/x)
    c1=int(c1)
    c2=0
    for i in range(n):
        c2+=math.ceil(a[i]/x)
    c2=int(c2)
    print(c1,c2)        

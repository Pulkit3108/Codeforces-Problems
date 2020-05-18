import math
n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    if(a[i]>=0):
        a[i]=-a[i]-1
if(n%2!=0):
    x=a.index(min(a))
    a[x]=-a[x]-1
for i in range(0,n):
    print(a[i],end=' ')

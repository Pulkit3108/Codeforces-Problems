import math
def check(x):
    y=int(math.sqrt(x))
    if(x==y*y):
        return False
    return True
n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(n-1,-1,-1):
    if(a[i]<0 or check(a[i])):
        print(a[i])
        break

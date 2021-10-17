import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if(a[0]==a[n-1]):
        print(-1)
    else:
        t=0
        for i in range(1,n):
            t=math.gcd(t,a[i]-a[0])
        print(t)


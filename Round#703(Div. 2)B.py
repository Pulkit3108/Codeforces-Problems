t=int(input())
for _ in range(t):
    n=int(input())
    x=list()
    y=list()
    for i in range(n):
        a,b=map(int,input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    if(n%2!=0):
        print(1)
    else:
        w=x[n//2]-x[n//2-1]+1
        s=y[n//2]-y[n//2-1]+1
        print(w*s)
        

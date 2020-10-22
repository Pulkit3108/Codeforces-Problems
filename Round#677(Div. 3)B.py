t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    p=list()
    for i in range(n):
        if(a[i]==1):
            p.append(i+1)
    f=1
    for i in range(len(p)-1):
        if(p[i]+1==p[i+1]):
            continue
        else:
            c+=(p[i+1]-p[i]-1)
    print(c)

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    m=-1e18
    for i in range(0,5):
        q=(n-5+i)%n
        w=(n-4+i)%n
        e=(n-3+i)%n
        r=(n-1+i)%n
        t=(n-2+i)%n
        p=a[q]*a[w]*a[e]*a[r]*a[t]
        m=max(m,p)
    print(m)

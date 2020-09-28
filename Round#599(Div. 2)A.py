t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a=a[::-1]
    m=0
    for i in range(0,n):
        k=min(i+1,a[i])
        m=max(m,k)
    print(m)    

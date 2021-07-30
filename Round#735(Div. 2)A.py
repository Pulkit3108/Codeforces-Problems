for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=-1
    for i in range(n-1):
        m=max(m,a[i]*a[i+1])
    print(m)

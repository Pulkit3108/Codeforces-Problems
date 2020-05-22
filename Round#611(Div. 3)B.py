T=int(input())
for _ in range(0,T):
    n,k=map(int,input().split())
    a=n//k
    b=a*k
    d=b
    c=n-b
    x=k//2
    d+=min(c,x)
    print(d)

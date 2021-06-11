for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=a.index(1)
    m=a.index(n)
    c1=max(l,m)+1
    c2=n-min(l,m)
    c3=min(l,m)+1+n-max(l,m)
    print(min(c1,c2,c3))
        

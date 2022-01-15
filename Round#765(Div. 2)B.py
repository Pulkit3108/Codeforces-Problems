for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    h=-1
    for i in range(n):
        if(a[i] in d):
            x=d[a[i]]
            h=max(h,n-i+x)
        d[a[i]]=i
    print(h)

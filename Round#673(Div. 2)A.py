t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=a.index(min(a))
    c=0
    for i in range(n):
        if(i!=m):
            while((a[i]+a[m])<=k):
                a[i]+=a[m]
                c+=1
    print(c)

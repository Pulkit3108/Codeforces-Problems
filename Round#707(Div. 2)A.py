t=int(input())
for _ in range(t):
    n=int(input())
    a=[0]*(n+1)
    b=[0]*(n+1)
    for i in range(1,n+1):
        a[i],b[i]=map(int,input().split())
    tm=list(map(int,input().split()))
    ar=0
    dp=0
    for i in range(1,n+1):
        t=abs(a[i]-b[i-1])
        ar=dp+t+tm[i-1]
        w=abs(a[i]-b[i])//2
        if((a[i]-b[i])%2!=0):
            w+=1
        dp=ar+w
        dp=max(dp,b[i])
    print(ar)
        

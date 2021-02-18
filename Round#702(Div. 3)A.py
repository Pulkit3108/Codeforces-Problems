t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=[0]*3
    k=0
    for i in range(n):
        c[a[i]%3]+=1
    q=n//3
    while(c[0]!=c[1] or c[1]!=c[2]):
        if(c[0]>q):
            d=c[0]-q
            c[0]=q
            k+=d
            c[1]+=d
        if(c[1]>q):
            d=c[1]-q
            c[1]=q
            k+=d
            c[2]+=d
        if(c[2]>q):
            d=c[2]-q
            c[2]=q
            k+=d
            c[0]+=d
    print(k)

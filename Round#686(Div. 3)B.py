t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*(n+1)
    c=[0]*(n+1)
    for i in range(n):
        b[a[i]]+=1
        c[a[i]]=i+1
    q=-1
    for i in range(n+1):
        if(b[i]==1):
            q=c[i]
            break
    print(q)
             

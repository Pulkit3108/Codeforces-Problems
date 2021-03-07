t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    r=k//2
    if(k%2!=0):
        r+=1
    c=(n-k)+(k-r)
    print(c)
    for i in range(r,k):
        print(i,end=' ')
    for i in range(k+1,n+1):
        print(i,end=' ')
    print()

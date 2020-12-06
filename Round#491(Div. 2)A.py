a,b,c,n=map(int,input().split())
if(c>b or c>a or c>n):
    print(-1)
else:
    k=c+(a-c)+(b-c)
    k=n-k
    if(k>0):
        print(k)
    else:
        print(-1)


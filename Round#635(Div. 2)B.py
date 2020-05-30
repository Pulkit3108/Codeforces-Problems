T=int(input())
for _ in range(T):
    x,n,m=map(int,input().split())
    c=x
    for i in range(n):
        if(c>20):
            c=c//2+10
    for j in range(m):
        c-=10
    if(c>0):
        print("NO")
    else:
        print("YES")

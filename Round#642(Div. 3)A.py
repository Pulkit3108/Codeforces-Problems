T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    ans=0
    if(n==2):
        ans=m
    if(n>2):
        ans=m*2
    print(ans)
        

T=int(input())
for _ in range(0,T):
    h,m=map(int,input().split())
    x=h*60+m
    ans=24*60-x
    print(ans)

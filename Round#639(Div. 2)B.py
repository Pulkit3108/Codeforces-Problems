def cal(n):
    if(n<2):
        return(0)
    else:
        h=1
        x=0
        c=1
        while(x<=n):
            x=(h*(h+1))+(h*(h-1))//2
            h+=1
        h=h-2
        x=(h*(h+1))+(h*(h-1))//2
        n=n-x
        return(c+cal(n))
T=int(input())
for _ in range(0,T):
    n=int(input())
    if(n<2):
        ans=0
    else:
        ans=cal(n)
    print(ans)

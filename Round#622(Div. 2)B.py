t=int(input())
for _ in range(0,t):
    n,x,y=list(map(int,input().split()))
    a=max(1,min(n,x+y-n+1))
    b=min(n,x+y-1)
    print(a,b)



    
    



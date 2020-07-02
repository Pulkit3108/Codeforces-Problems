t=int(input())
for _ in range(0,t):
    a,b,n,m=map(int,input().split())
    if(m>min(a,b) or (n+m)>(a+b)):
        print("No")
    else:
        print("Yes")

    
    



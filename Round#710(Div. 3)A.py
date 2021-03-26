t=int(input())
for _ in range(t):
    n,m,x=map(int,input().split())
    c=x//n
    r=(x-1)%n
    if(x%n==0):
        c-=1
    a=c+1
    if(r!=0):
        a+=r*m
    print(a)
    
    
        

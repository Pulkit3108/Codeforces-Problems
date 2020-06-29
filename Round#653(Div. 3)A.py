t=int(input())
for _ in range(0,t):
    x,y,n=map(int,input().split())
    a=n%x
    k=0
    q=0
    r=0
    if(a==y):
        k=n
    else:
        r=y-a
        if(r>0):
            q=a+(x-y)
            k=n-q
        else:
            k=n-(a-y)
    print(k)
        
    

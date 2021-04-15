t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=min(a)
    c=0
    flag=False
    for i in a:
        if(i==m):
            c+=1
        if(i&m!=m):
            flag=True
            break
    if(flag):
        print(0)
    else:
        mod=int(1e9+7)
        f=1
        for i in range(1,n-1):
            f=(f*i)%mod
        k=f*c*(c-1)%mod
        print(k)
            
        
                
    

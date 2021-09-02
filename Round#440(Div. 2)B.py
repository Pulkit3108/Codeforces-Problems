n,k=map(int,input().split())
a=list(map(int,input().split()))
if(k==1):
    print(min(a))
elif(k==2):
    b=[0]*n
    b[n-1]=a[n-1];
    for i in range(n-2,-1,-1):
        b[i]=min(a[i],b[i+1])
    x=a[0]
    t=max(x,b[1])
    for i in range(1,n-1):
        x=min(x,a[i]);
        t=max(t,max(b[i+1],x))
    print(t)
else:
    print(max(a))
    

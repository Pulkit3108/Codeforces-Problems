def broke(n):
    x=n
    N=0
    while(x!=0):
        x=x//10
        N+=1
    A=[0]*N
    i=0
    while(n!=0):
        A[i]=n%10
        n=n//10
        i+=1
    return(A)
l,r=map(int,input().split())
k=0
for i in range(l,r+1):
    X=broke(i)
    a=len(X)
    Y=set(X)
    b=len(Y)
    if(a==b):
        k=1
        print(i)
        break;
if(k==0):
    print(-1)


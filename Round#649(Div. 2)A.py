T=int(input())
for _ in range(0,T):
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    c1=-1
    c2=0
    s=sum(A)
    for i in range(0,n):
        if(A[i]%x!=0):
            if(c1==-1):
                c1=i
            c2=i
    if(s%x!=0):
        print(n)
    elif(c1==-1):
        print(-1)
    else:
        k=min(c1+1,n-c2)
        print(n-k)
   


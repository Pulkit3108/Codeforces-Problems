n,k=map(int,input().split())
if(n==k or k==0):
    print(0,0)
else:
    if(3*k>=n):
        print(1,n-k)
    else:
        print(1,2*k)

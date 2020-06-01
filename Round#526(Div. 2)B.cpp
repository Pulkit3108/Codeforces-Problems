n,s=map(int,input().split())
A=list(map(int,input().split()))
a=0
ans=0
if(sum(A)<s):
    ans=-1
else:
    x=min(A)
    for i in range(0,n):
        if(A[i]!=x):
            a+=A[i]-x
    if(a>=s):
        ans=x
    else:
        c=s-a+n-1
        c=c//n
        ans=x-c
print(ans)

        

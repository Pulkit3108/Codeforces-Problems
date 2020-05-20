n,x,y=map(int,input().split())
A=list(map(int,input().split()))
ans=0
for i in range(0,n):
    a=b=1
    c1=x
    c2=y
    j=i-1
    k=i+1
    while(j>0 and c1>0):
        if(A[j]<A[i]):
            a=0
            break
        j-=1
        c1-=1
    while(k<n and c2>0):
        if(A[k]<A[i]):
            b=0
            break
        k+=1
        c2-=1
    if(a==1 and b==1):
        ans=i+1
        break
print(ans)

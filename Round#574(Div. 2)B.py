def sos(n):
    return(n*(n+1)//2)
n,k=map(int,input().split())
l,h,m,a=0,n,0,0
while(l<=h):
    m=(l+h)//2
    if(sos(m)-(n-m)==k):
        a=n-m
        break
    elif(sos(m)-(n-m)<k):
        l=m+1
    else:
        h=m-1
print(a)

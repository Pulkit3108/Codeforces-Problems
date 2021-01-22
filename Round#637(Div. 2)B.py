t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    mn=1
    mx=0
    for i in range(1,k-1):
        if(a[i]>a[i-1] and a[i]>a[i+1]):
            mx+=1
    l=mx
    for i in range(k,n):
        p=l
        if(a[i-k+1]>a[i-k] and a[i-k+1]>a[i-k+2]):
            p-=1
        if(a[i-1]>a[i-2] and a[i-1]>a[i]):
            p+=1
        if(p>mx):
            mx=p
            mn=i-k+2
        l=p
    print(mx+1,mn)
    

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d=[0]*n
    k=0
    for i in range(n-1,-1,-1):
        k=max(k,a[i])
        if(k!=0):
            a[i]=1
            k-=1
        else:
            a[i]=0
    print(' '.join(map(str,a)))
        

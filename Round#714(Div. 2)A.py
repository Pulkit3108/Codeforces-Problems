t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    f=0
    f=n//2
    if(n%2==0):
        f-=1
    if((n<3 and k!=0) or k>f):
        print(-1)
    else:
        a=list(range(1,n+1))
        j=1
        while(k!=0):
            a.insert(j,a[n-1])
            j+=2
            a.pop(n)
            k-=1
        print(' '.join(map(str,a)))

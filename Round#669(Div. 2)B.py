def gcd(a,b):
    if(b==0):
        return(a)
    else:
        return(gcd(b,a%b))
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list()
    v=[0]*n
    m=max(a)
    v[a.index(m)]=1
    b.append(m)
    d=m
    for i in range(n):
        r=0
        k=0
        for j in range(n):
            if(v[j]==1):
                continue
            elif(gcd(d,a[j])>k):
                r=j
                k=gcd(d,a[j])
        d=k
        v[r]=1
        b.append(a[r])
    print(' '.join(map(str,b[:n])))
    

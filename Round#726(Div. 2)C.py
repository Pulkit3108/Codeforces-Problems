for _ in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    h.sort()
    d=h[1]-h[0]
    x=0
    y=1
    for i in range(1,n-1):
        if(h[i+1]-h[i]<d):
            d=h[i+1]-h[i]
            x=i
            y=i+1 
    a=[0]*n
    a[0]=h[x]
    j=1
    for i in range(y+1,n):
        a[j]=h[i]
        j+=1
    for i in range(0,x):
        a[j]=h[i]
        j+=1
    a[n-1]=h[y]
    print(' '.join(map(str,a)))



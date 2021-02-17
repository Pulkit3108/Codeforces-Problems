t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    c=0
    while(i!=n-1):
        ma=max(a[i],a[i+1])
        mi=min(a[i],a[i+1])
        if(ma<=2*mi):
            i+=1
        else:
            c+=1
            k=ma//2
            if(ma%2!=0):
                k+=1
            a.insert(i+1,k)
            n+=1
    print(c)
            

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    i=0
    while(k!=0 and i!=n-1):
        if(k>a[i]):
            k-=a[i];
            a[n-1]+=a[i];
            a[i]=0;
        else:
            a[i]-=k;
            a[n-1]+=k;
            k=0;
        i+=1
    print(' '.join(map(str,a)))

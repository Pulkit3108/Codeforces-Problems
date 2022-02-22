for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(1,n-1):
        if(a[i]>a[i-1] and a[i]>a[i+1]):
            if(i+2<n):
                a[i+1]=max(a[i],a[i+2]);
            else:
                a[i+1]=a[i];
            c+=1;
    print(c)
    print(*a)





        

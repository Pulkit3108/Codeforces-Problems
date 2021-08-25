for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    c=0
    while(a!=b):
        c+=1
        if(c&1):
            for i in range(0,n-2,2):
                if(a[i]>a[i+1]):
                    a[i],a[i+1]=a[i+1],a[i]
        else:
            for i in range(1,n-1,2):
                if(a[i]>a[i+1]):
                    a[i],a[i+1]=a[i+1],a[i]            
    print(c)
    
    

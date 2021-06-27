for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(1,n+1):
        for j in range(a[i-1]-i,n+1,a[i-1]):
            if(a[i-1]*a[j-1]==i+j and i<j):
                c+=1
    print(c)
    

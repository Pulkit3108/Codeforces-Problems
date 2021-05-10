for _ in range(int(input())):
    n=int(input())
    c=0
    i=1
    while(i<n+1):
        for j in range(1,10):
            if(i*j<=n):
                c+=1
        i=i*10+1
    print(c)
    
    

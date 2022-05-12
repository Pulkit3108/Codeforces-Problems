for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=min(a)
    s=0
    for i in range(n):
        s+=a[i]-m
    print(s)
    
    
        
        
    
    

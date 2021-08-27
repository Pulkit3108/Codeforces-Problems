for _ in range(int(input())):
    l,r=map(int,input().split())
    d=r-l
    m=0
    if(r&1):
        m=r//2
    else:
        m=r//2-1
    print(min(m,d))
    

    

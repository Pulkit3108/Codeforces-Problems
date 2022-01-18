for _ in range(int(input())):
    n,m=map(int,input().split())
    d=list()
    for x in range(n): 
        for y in range(m):
            d.append(max(x,n-1-x)+max(y,m-1-y))
    print(*sorted(d))
    
            


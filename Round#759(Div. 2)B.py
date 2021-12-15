for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    e=0
    c=a[-1]
    for i in range(n-1,-1,-1):
        if(a[i]>c):
            c=a[i]
            e+=1
        if(c==m):
            break 
    print(e)

        
        
        

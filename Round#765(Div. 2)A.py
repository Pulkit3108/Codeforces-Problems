for _ in range(int(input())):
    n,l=map(int,input().split())
    x=list(map(int,input().split()))
    y=0
    for i in range(l):
        c=0
        for j in x:
            if(j&(1<<i)):
                c+=1
        if(c>n-c):
            y+=1<<i
    print(y)
    

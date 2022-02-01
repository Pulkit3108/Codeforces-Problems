for _ in range(int(input())):
    n=int(input())
    b=n-1
    for i in range(30,-1,-1):
        if(b&(1<<i)):
            break
    m=(1<<i)-1
    for i in range(n-1,m,-1):
        print(i,end=' ')
    for i in range(0,m+1,1):
        print(i,end=' ')
    print()
        

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    flag=False
    s=sum(a)
    for i in range(n):
        c=(s-a[i])/(n-1)
        if(c==a[i]):
            flag=True
            break
    if(flag):
        print('YES')
    else:
        print('NO')

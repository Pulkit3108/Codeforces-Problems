for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(n&1):
        flag=False
        for i in range(n-1):
            if(a[i+1]<=a[i]):
                flag=True
                break
        if(flag):
            print('YES')
        else:
            print('NO')
    else:
        print('YES')

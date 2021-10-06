for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=sorted(a)
    if(n>=(2*x)):
        print('YES')
    else:
        if(b[n-x:x]==a[n-x:x]):
            print('YES')
        else:
            print('NO')

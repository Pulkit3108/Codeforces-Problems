for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    c=n+max(a[0],a[n-1])
    for i in range(1,n):
        c+=max(a[i-1],a[i])
    if(c>m):
        print('NO')
    else:
        print('YES')    

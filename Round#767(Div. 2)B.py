for _ in range(int(input())):
    l,r,k=map(int,input().split())
    if(l==1 and r==1):
        print('NO')
    else:
        c=(r-l+1)-(r//2-(l-1)//2)
        if(l==r or c<=k):
            print('YES')
        else:
            print('NO')


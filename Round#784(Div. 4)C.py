for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(n==2):
        print('YES')
    else:
        flag=False
        for i in range(2,n):
            if((a[i-2]&1)!=(a[i]&1)):
                flag=True
                break
        if(flag):
            print('NO')
        else:
            print('YES')

    

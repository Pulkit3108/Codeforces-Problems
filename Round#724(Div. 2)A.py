for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=1
    for i in a:
        if(i<0):
            c=0
            break
    if(c==0):
        print('NO')
    else:
        print('YES')
        print(101)
        print(' '.join(map(str,range(101))))
        

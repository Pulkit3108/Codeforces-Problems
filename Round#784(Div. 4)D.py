for _ in range(int(input())):
    n=int(input())
    s=input().split('W')
    flag=False
    for i in s:
        if(len(i)!=0 and ('R' not in i or 'B' not in i)):
            flag=True
            break
    if(flag):
        print('NO')
    else:
        print('YES')

    

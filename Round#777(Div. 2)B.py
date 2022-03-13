for _ in range(int(input())):
    n,m=map(int,input().split())
    r=list()
    for _ in range(n):
        s=input()
        r.append(s)
    flag=True
    for i in range(n-1):
        for j in range(m-1):
            s=int(r[i][j])+int(r[i][j+1])+int(r[i+1][j])+int(r[i+1][j+1])
            if(s==3):
                flag=False
                break
        if(flag==False):
            break
    if(flag):
        print('YES')
    else:
        print('NO')



        

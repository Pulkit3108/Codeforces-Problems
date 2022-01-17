for _ in range(int(input())):
    n,m,r,c=map(int,input().split())
    s=list()
    for _ in range(n):
        s.append(input())
    if(s[r-1][c-1]=='B'):
        print(0)
        continue
    flag=False
    for i in range(n):
        if('B' in s[i]):
            flag=True
            break
    if(flag):
        t=2
        for i in range(n):
            if(s[i][c-1]=='B'):
                t=1
                break
        for j in range(m):
            if(s[r-1][j]=='B'):
                t=1
                break
        print(t)
    else:
        print(-1)
    
            


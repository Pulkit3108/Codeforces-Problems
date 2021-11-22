n=int(input())
a=list()
for _ in range(n):
    b=list(map(int,input().split()))
    a.append(b)
flag=True
for i in range(n):
    for j in range(n):
        if(a[i][j]==1): 
            continue
        flag=False
        for r in range(n):
            if(r==i):
                continue
            for c in range(n):
                if(c==j): 
                    continue
                s=a[r][j]+a[i][c]
                if(s==a[i][j]):
                    flag=True
                    break
            if(flag):
                break
        if(not flag):
            break
    if(not flag):
        break
if(flag):
    print('Yes')
else:
    print('No')
            


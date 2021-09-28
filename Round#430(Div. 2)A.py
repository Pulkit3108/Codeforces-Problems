l,r,x,y,k=map(int,input().split())
flag=False
for i in range(x,y+1):
    if(i*k<=r and i*k>=l):
        flag=True
        break
if(flag):
    print('YES')
else:
    print('NO')



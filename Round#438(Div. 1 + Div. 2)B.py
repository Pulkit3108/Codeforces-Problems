h,m,s,t1,t2=map(int,input().split())
c=[0]*3600*12
h=h%12
t1=t1%12
t2=t2%12
c[3600*h+60*m+s]=1
c[720*m+12*s]=1
c[720*s]=1
t1,t2=min(t1,t2),max(t1,t2)
t1*=3600
t2*=3600
flag=False
for i in range(t1+1,t2):
    if(c[i]):
        flag=True
        break
if(not flag):
    print('YES')
else:
    flag=False
    for i in range(3600*12-1,t2,-1):
        if(c[i]):
            flag=True
            break
    for i in range(t1):
        if(c[i]):
            flag=True
            break
    if(not flag):
        print('YES')
    else:
        print('NO')


 

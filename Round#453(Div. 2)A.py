n,m=map(int,input().split())
a=list()
b=list()
for _ in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
l=a[0]
r=b[0]
c=1
for i in range(1,n):
    if(a[i]>r or b[i]<l):
        c=0
        break
    l=min(l,a[i])
    r=max(r,b[i])
if(c and l==0 and r==m):
    print('YES')
else:
    print('NO')    
        

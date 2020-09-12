n,h,m=map(int,input().split())
l=list()
r=list()
x=list()
for i in range(m):
    a,b,c=map(int,input().split())
    l.append(a)
    r.append(b)
    x.append(c)
Z=[0]+[h]*n
c=0
for i in range(m):
    for j in range(l[i],r[i]+1):
        Z[j]=min(x[i],Z[j])
s=0
for i in Z:
    s+=i*i
print(s)

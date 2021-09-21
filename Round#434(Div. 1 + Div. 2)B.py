n,m=map(int,input().split())
k=list()
f=list()
for _ in range(m):
    x,y=map(int,input().split())
    k.append(x)
    f.append(y)
a=set()
for i in range(1,101):
    for j in range(m):
        q=(f[j]-1)*i+1
        e=f[j]*i
        if(k[j]<q or k[j]>e):
            break
    else:
        a.add((n+i-1)//i)
if(len(a)>1):
    print(-1)
else:
    print(*a)
  

n,L,a=map(int,input().split())
t=list()
l=list()
for _ in range(0,n):
    a1,b1=map(int,input().split())
    t.append(a1)
    l.append(b1)
if(n==0):
    print(L//a)
else: 
    c1=0
    c2=0
    for i in range(0,n):
        c2+=(t[i]-c1)//a
        c1=t[i]+l[i]
    c2+=(L-c1)//a
    print(c2)




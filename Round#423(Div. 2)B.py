n,m=map(int,input().split())
s=list()
for _ in range(n):
    t=input()
    s.append(t)
x1,y1=float("inf"),float("inf")
x2,y2=float("-inf"),float("-inf")
c=0
for i in range(n):
    for j in range(m):
        if(s[i][j]=='B'):
            c+=1
            x1=min(x1,i)
            y1=min(y1,j)
            x2=max(x2,i)
            y2=max(y2,j)
if(c==0):
    print(1)
else:
    p=0
    l=max(x2-x1+1,y2-y1+1)
    if(l>n or l>m):
        p=-1
    else:
        p=l*l-c
    print(p)

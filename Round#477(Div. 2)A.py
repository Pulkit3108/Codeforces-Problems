n,s=map(int,input().split())
h=list()
m=list()
l=list()
l.append(0)
for _ in range(n):
    x,y=map(int,input().split())
    h.append(x)
    m.append(y)
    l.append((x*60)+y)
if(l[1]!=0 and (l[1]-l[0])>=s+1):
    print(0,0)
else:
    k=2*s+2
    r=0
    for i in range(n):
        if(l[i+1]-l[i]>=k):
            r=l[i]+s+1
            break
        else:
            continue
    if(r==0):
        r=l[n]+s+1    
    print(r//60,r%60)
    

n,m=map(int,input().split())
l=list()
r=list()
for _ in range(m):
    a,b=map(int,input().split())
    l.append(a)
    r.append(b)
for i in range(n):
    if(i%2==0):
        print(0,end='')
    else:
        print(1,end='')
    

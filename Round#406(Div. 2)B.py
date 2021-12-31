n,m=map(int,input().split())
flag=False
for _ in range(m):
    g=set(list(map(int,input().split()))[1:])
    v=set(abs(i) for i in g)
    if(len(v)!=len(g)):
        continue
    else:
        flag=True
if(flag):
    print("YES")
else:
    print("NO")

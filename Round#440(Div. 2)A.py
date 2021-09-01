n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
flag=True
a.sort()
b.sort()
for i in a:
    if(i in b):
        print(i)
        flag=False
        break
if(flag):
    print(min(a[0],b[0])*10+max(a[0],b[0]))

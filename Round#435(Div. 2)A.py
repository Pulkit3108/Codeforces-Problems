n,x=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*105
for i in a:
    b[i]=1
c=b[x]
for i in range(x):
    c+=(b[i]==0)
print(c)

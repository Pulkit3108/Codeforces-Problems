m,b=map(int,input().split())
r=-1
for i in range(b):
    x=(b-i)*m;
    s=(i+x)*(x+1)*(i+1)
    r=max(r,s)
print(r//2)


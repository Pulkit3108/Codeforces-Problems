x,y,z=map(int,input().split())
x1=x%z
y1=y%z
s=x//z+y//z
if(x1+y1<z):
    print(s,0)
else:
    print(s+1,min(z-x1,z-y1))

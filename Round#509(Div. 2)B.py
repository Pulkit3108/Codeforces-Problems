import math
a,b,x,y=map(int,input().split())
e=math.gcd(x,y)
x=x//e
y=y//e
c=0
if(x>a or y>b):
    c=0
else:
    q=a//x
    w=b//y
    c=min(q,w)
print(c)

import math
n,t,k,d=map(int,input().split())
t1=math.ceil(n/k)*t
if (t1-t>d):
    print('YES')
else: 
    print('NO')

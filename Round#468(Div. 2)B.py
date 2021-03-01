import math
n,a,b=map(int,input().split())
k=int(math.log(n,2))
r=0
for i in range(k):
    if(a%2!=0):
        a+=1
    if(b%2!=0):
        b+=1
    a=a//2
    b=b//2
    r+=1
    if(a==b):
        break
if(r==k):
    print('Final!')
else:
    print(r)

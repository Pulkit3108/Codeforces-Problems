import math
n,k=map(int,input().split())
w=list(map(int,input().split()))
d=0
for i in w:
    d+=math.ceil(i/k)   
print(math.ceil(d/2))

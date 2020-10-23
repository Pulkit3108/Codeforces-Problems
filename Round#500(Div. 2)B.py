n,x=map(int,input().split())
a=list(map(int,input().split()))
A=set()
B=set()
z=0
o=0
t=0
for i in range(n):
    if(a[i] in B):
        z=1
    if(a[i] in A):
        o=1
    if(a[i]&x in B):
        o=1
    if(a[i]&x in A):
        t=1
    B.add(a[i])
    A.add(a[i]&x)
if(z):
    print(0)
elif(o):
    print(1)
elif(t):
    print(2)
else:
    print(-1)
        
        
            

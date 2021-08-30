n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=0
n-=1
if(n>0):
    d+=min(a,b)
    n-=1
if(n>0):
    d+=min(d,c)*n
print(d)


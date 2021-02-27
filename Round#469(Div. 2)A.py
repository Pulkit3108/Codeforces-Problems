l,r,a=map(int,input().split())
m=2*min(l,r)
x=abs(l-r)
k=min(x,a)
z=2*k
a=max(0,a-k)//2
m=2*a+m+z
print(m)

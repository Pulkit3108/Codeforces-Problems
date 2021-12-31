inf=1e9+10
mn1=mn2=inf
mx1=mx2=-inf
for i in range(int(input())):
    l,r=map(int,input().split())
    mx1=max(mx1,l)
    mn1=min(mn1,r)
for i in range(int(input())):
    l,r=map(int,input().split())
    mx2=max(mx2,l)
    mn2=min(mn2,r)
c=max(mx2-mn1,mx1-mn2)
print(max(c,0))

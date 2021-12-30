n,m,k=map(int,input().split())
a=list(map(int,input().split()))
d=1e9+10
for i in range(n):
    if(a[i]!=0 and a[i]<=k):
        d=min(d,abs(m-(i+1)))
print(d*10)

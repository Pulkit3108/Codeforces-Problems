n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c1=float('inf')
for i in range(n):
    c2=float('-inf')
    for j in range(n):
        if(i!=j):
            for k in range(m):
                c2=max(c2,a[j]*b[k])
    c1=min(c1,c2)
print(c1)

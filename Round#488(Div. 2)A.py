n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
l=list()
for i in range(m):
    for j in range(n):
        if(y[i]==x[j]):
            l.append(j)
print(' '.join(map(str,[x[i] for i in sorted(l)])))

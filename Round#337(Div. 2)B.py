n=int(input())
a=list(map(int,input().split()))
m=min(a)
b=[i for i in range(n) if a[i]==m]
c=float('-inf')
for i in b:
    j=(i+1)%n
    t=n*m
    while(a[j]!=m):
        j=(j+1)%n
        t+=1
    c=max(c,t)
print(c)

mod=1000000007
n=int(input())
x=sorted(list(map(int,input().split())))
s=sum(x)
p=[]
j=1
for i in range(n+1):
    p.append(j)
    j=(j*2)%mod
d=0
for i in range(n):
    d=(d+(x[i]*p[i])%mod)%mod
    d=(d-(x[i]*p[n-i-1])%mod)%mod
print(int(d))


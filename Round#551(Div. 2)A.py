N,T=map(int,input().split())
S=[0]*N
D=[0]*N
x=0
ans=0
X=100000000000
m=0
for i in range(0,N):
    S[i],D[i]=map(int,input().split())
for i in range(0,N):
    if(S[i]>=T):
        if(X>S[i]):
            X=S[i]
            ans=i+1
    else:
        x=T-S[i]
        if(x%D[i]==0):
            x=x//D[i]
        else:
            x=x//D[i]+1
        m=S[i]+x*D[i]
        if(X>m):
            X=m
            ans=i+1
print(ans)

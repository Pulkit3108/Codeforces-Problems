n,m,k=map(int,input().split())
p=list(map(int,input().split()))
s=list(map(int,input().split()))
c=list(map(int,input().split()))
c1=0
for i in c:
    a=p[i-1]
    b=s[i-1]
    X=list()
    for j in range(0,n):
        if(b==s[j]):
            X.append(p[j])
    if(a<max(X)):
        c1+=1
print(c1)

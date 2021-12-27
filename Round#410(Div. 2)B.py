n=int(input())
s=list()
for _ in range(n):
    x=input()
    s.append(x) 
l=len(s[0])
flag=True
c=1e9+10
for i in range(0,n):
    if(len(s[i])!=l):
        flag=False
        break
    t=s[i]*2
    if(s[0] not in t):
        flag=False
        break
    f=0
    for j in range(n):
        x=l+1
        for k in range(l):
            if(s[i]==s[j][k:l]+s[j][0:k]):
                x=min(x,k)
        f+=x
    c=min(c,f)
if(flag):
    print(c)
else:
    print(-1)
    

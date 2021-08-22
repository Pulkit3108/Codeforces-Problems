s=list()
d=list()
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    s.append(a)
    d.append(b)
n=s[0]
for i in range(1,t):
    k=n-s[i]
    if(k<0):
        n=s[i]
    else:
        k+=1
        q=k//d[i]
        if(k%d[i]!=0):
            q+=1
        n=s[i]+(q*d[i])  
print(n)
    
    
    

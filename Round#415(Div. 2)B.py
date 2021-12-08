n,f=map(int,input().split())
t=list()
for _ in range(n):
    k,l=map(int,input().split())
    d=min(l,2*k)-min(l,k)
    t.append((k,l,d))
t.sort(key=lambda x:x[2],reverse=True)
p=0
for i in range(f):
    k,l,d=t[i]
    p+=min(l,2*k)
for i in range(f,n):
    k,l,d=t[i]
    p+=min(l,k)
print(p)

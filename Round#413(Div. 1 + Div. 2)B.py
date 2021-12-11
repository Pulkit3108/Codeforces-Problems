n=int(input())
p=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=int(input())
c=list(map(int,input().split()))
t=list()
for i in range(n):
    t.append([p[i],a[i],b[i]])
t=sorted(t,key=lambda x:x[0])
s=list()
k=[0]*4
for i in range(m):
    co=c[i]
    while(k[co]<n):
        if(t[k[co]][1]==co or t[k[co]][2]==co):
            s.append(t[k[co]][0])
            t[k[co]][1]=0
            t[k[co]][2]=0
            break
        k[co]+=1
    if(k[co]==n):
        s.append(-1)
print(*s)

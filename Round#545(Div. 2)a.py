n=int(input())
t=list(map(int,input().split()))
a=list()
c=1
for i in range(1,n):
    if(t[i]==t[i-1]):
        c+=1
    else:
        a.append(c)
        c=1
    if(i==n-1):
        a.append(c)
m=a[0]
r=0
for i in range(1,len(a)):
    m=min(a[i],a[i-1])
    r=max(r,m)
if(len(a)<2):
    r=0
print(r*2)

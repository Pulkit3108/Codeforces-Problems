n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c1=[0]*5
c2=[0]*5
for i in range(n):
    c1[a[i]-1]+=1
    c2[b[i]-1]+=1
s=0
flag=True
for i in range(5):
    if((c1[i]+c2[i])&1):
        flag=False
        break
    else:
        s+=abs(c1[i]-c2[i])
if(flag):
    print(s//4)
else:
    print(-1)

a,b,c=map(int,input().split())
r=a%b
t=b
cnt=1
f=0
while(t!=0):
    r*=10
    k=r//b
    r=r%b
    if(k==c):
        f=1
        break
    cnt+=1
    t-=1
if(f):
    print(cnt)
else:
    print(-1)

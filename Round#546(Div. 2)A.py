n=int(input())
L=list()
R=list()
for _ in range(0,n):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
k=int(input())
for i in range(0,n):
    if(k<=R[i]):
        break
ans=n-i
print(ans)


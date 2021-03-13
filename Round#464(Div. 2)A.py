n=int(input())
f=list(map(int,input().split()))
c=0
for i in range(n):
    if(f[f[f[i]-1]-1]-1==i):
        c=1
        break
if(c==1):
    print('YES')
else:
    print('NO')

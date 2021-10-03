n,k=map(int,input().split())
s=input()
d=dict()
for i in s:
    d[i]=d.get(i,0)+1
m=0
for _,i in d.items():
    m=max(m,i)
if(m>k):
    print('NO')
else:
    print('YES')

    

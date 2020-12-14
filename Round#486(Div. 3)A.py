n,k=map(int,input().split())
a=list(map(int,input().split()))
w=list()
q=list()
for i in range(n):
    if(a[i] not in q):
        q.append(a[i])
        w.append(i+1)
if(len(q)<k):
    print('NO')
else:
    print('YES')
    print(' '.join(map(str,w[:k])))
    
    

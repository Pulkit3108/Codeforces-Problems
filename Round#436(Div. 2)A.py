n=int(input())
a=list()
for _ in range(n):
    x=int(input())
    a.append(x)
a.sort()
if(a[0]==a[n//2-1] and a[n//2]==a[n-1] and a[0]!=a[n-1]):
    print('YES')
    print(a[0],a[n//2])
else:
    print('NO')

    

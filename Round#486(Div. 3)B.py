n=int(input())
s=list()
for i in range(n):
    x=input()
    s.append(x)
a=sorted(s,key=len)
c=1
for i in range(n-1):
    if(a[i] not in a[i+1]):
        c=0
        break
if(c==0):
    print('NO')
else:
    print('YES')
    for i in range(n):
        print(a[i])

import sys
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m=sys.maxsize
    for i in range(n):
        if(b[i]!=0):
            m=min(m,a[i]-b[i])
    if(m<0):
        print('NO')
        continue
    flag=True
    for i in range(n):
        if((b[i]!=0 and m>a[i]-b[i]) or m<a[i]-b[i]):
            flag=False
            break
    if(flag):
        print('YES')
    else:
        print('NO')
        

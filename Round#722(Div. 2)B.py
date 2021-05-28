import sys
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c=1
    m=sys.maxsize
    for i in range(1,n):
        m=min(m,abs(a[i]-a[i-1]))
        if(m<a[i]):
            break
        c+=1
    print(c)
    

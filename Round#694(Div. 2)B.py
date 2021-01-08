import sys
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    b=[0]*n
    j=0
    m=sys.maxsize
    for i in range(n):
        q=a[i]
        while(q%x==0):
            b[i]+=1
            q=q//x
        if(b[i]<m):
            m=b[i]
            j=i
    s=((b[j]+1)*sum(a))+sum(a[:j])
    print(s)

            

for _ in range(int(input())):
    n=int(input())
    q=list(map(int,input().split()))
    b=[-1]*n
    for i in range(n):
        if(b[q[i]-1]==-1):
            b[q[i]-1]=i
    p=[-1]*n
    c=[]
    for i in range(n):
        if(b[i]!=-1):
            p[b[i]]=i+1
        else:
            c.append(i+1)
    j=0
    for i in range(n):
        if(p[i]==-1):
            p[i]=c[j]
            j+= 1
    m=-1
    flag=True
    for i in range(n):
        m=max(m,p[i])
        if(m!=q[i]):
            flag=False
    if(flag):
        print(*p)
    else:
        print(-1)
        

for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    d=dict()
    for i,j in enumerate(s):
        if(d.get(j) is not None):
            d[j].append(i+1)
        else:
            d[j]=[i+1]
    flag=True
    for k,v in d.items():
        if(len(v)==1):
            flag=False
            break
        else:
            for i in range(len(v)):
                s[v[i]-1]=v[(i+1)%len(v)]
    if(flag):
        print(*s)
    else:
        print(-1)
    

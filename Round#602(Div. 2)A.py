t=int(input())
for _ in range(t):
    n=int(input())
    l=list()
    r=list()
    for i in range(n):
        a,b=map(int,input().split())
        l.append(a)
        r.append(b)
    print(max(0,(max(l)-min(r))))

    
R

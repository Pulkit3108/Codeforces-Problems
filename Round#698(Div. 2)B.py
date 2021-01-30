t=int(input())
for _ in range(t):
    q,d=map(int,input().split())
    a=list(map(int,input().split()))
    m1=[ str(d*i) for i in range(1,11) ]
    m2=[ i[-1] for i in m1 ]
    for i in range(q):
        s=-100
        k=str(a[i])
        for j in range(10):
            if(m2[j]==k[-1]):
                s=j
                break
        if(s<0 or int(m1[s])>a[i]):
            print('NO')
        else:
            print('YES')
            
       #

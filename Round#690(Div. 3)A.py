t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    a=list()
    e=0
    o=n-1
    for i in range(n):
        if(i%2==0):
            a.append(b[e])
            e+=1
        else:
            a.append(b[o])
            o-=1
    print(' '.join(map(str,a)))

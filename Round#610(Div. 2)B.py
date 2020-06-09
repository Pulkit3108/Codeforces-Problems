T=int(input())
for _ in range(0,T):
    n,p,k=map(int,input().split())
    A=list(map(int,input().split()))
    q=p
    A.sort()
    c1=0
    c2=0
    for i in range(1,n,2):
        if(p>=A[i]):
            c1+=2
            p-=A[i]
        else:
            break
    if(q>=A[0]):
        q-=A[0]
        c2+=1
        for i in range(2,n,2):
            if(q>=A[i]):
                c2+=2
                q-=A[i]
            else:
                break
    print(max(c1,c2))

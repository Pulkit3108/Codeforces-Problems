t=int(input())
for _ in range(t):
    A=list(map(int,input().split()))
    A.sort()
    c1=0
    c2=0
    q=0
    if(A[0]+A[1]>A[2]):
        c1=A[2]
        c2=A[1]
        q=A[0]-(c1-c2)
        if(q>0):
            c1+=q//2
            c2+=(q-q//2)+(c1-c2)
    else:
        c1=A[1]
        c2=A[0]
        q=A[2]-(c1-c2)
        if(q>0):
            c1+=q//2
            c2+=(q-q//2)+(c1-c2)
    print(min(c1,c2))



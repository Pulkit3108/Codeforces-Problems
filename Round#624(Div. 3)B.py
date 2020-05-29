T=int(input())
for _ in range(T):
    count=0
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    P=list(map(int,input().split()))
    while(1):
        x=0
        for i in range(0,n-1):
            if(A[i]>A[i+1]):
                if i+1 in P:
                    x=1
                    t=A[i]
                    A[i]=A[i+1]
                    A[i+1]=t
        if(x==0):
            break
    if(A==sorted(A)):
        print("YES")
    else:
        print("NO")

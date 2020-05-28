T=int(input())
for _ in range(T):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    B=B[::-1]
    for i in range(0,k):
        if(A[i]<B[i]):
            A[i]=B[i]
        else:
            break
    print(sum(A))        

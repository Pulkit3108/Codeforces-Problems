T=int(input())
for _ in range(0,T):
    A=list(map(int,input().split()))
    A.sort()
    if(2*A[0]>A[1]):
        print(2*A[0]*A[0]*2)
    else:
        print(A[1]*A[1])

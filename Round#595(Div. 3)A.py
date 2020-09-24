t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    c=0
    A.sort()
    for i in range(1,n):
        if(A[i]-A[i-1]<2):
            c=1
            break
    if(c==0):
        print(1)
    else:
        print(2)


t=int(input())
for _ in range(0,t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    a=min(A)
    b=min(B)
    c=0
    for i in range(0,n):
        if(A[i]!=a and B[i]!=b):
            x=min(A[i]-a,B[i]-b)
            A[i]-=x
            B[i]-=x
            c+=x
    for i in range(0,n):
        if(A[i]!=a):
            x=A[i]-a
            A[i]-=x
            c+=x
        if(B[i]!=b):
            x=B[i]-b
            B[i]-=x
            c+=x
    print(c)

from math import gcd
def getprime(x):
    for i in range(2, x):
        if(x%i==0):
            return(i)
    return(-1)
P=[2,3,5,7,11,13,17,19,23,29,31]
T=int(input())
for _ in range(0,T):
    N=int(input())
    A=list(map(int,input().split()))
    C=[0]*11
    M=list()
    for i in range(N):
        x=P.index(getprime(A[i]))
        C[x]=1
        M.append(x)
    c=0
    X=list()
    for i in range(0,11):
        X.append(c)
        if(C[i]):
            c+=1
    print(c)
    for i in range(0,N):
        x=P.index(getprime(A[i]))
        print(X[x]+1,end=" ")
    print()

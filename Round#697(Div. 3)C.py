t=int(input())
for _ in range(t): 
    a,b,k=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A1=[0]*(a+1)
    B1=[0]*(b+1)
    for i in A:
        A1[i]+=1
    for i in B:
        B1[i]+=1
    T=0
    for i in range(k):
        T+=(k-1)-(A1[A[i]]-1)-(B1[B[i]]-1)
    print(T//2)

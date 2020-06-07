T=int(input())
for _ in range(0,T):
    N=int(input())
    A=list(map(int,input().split()))
    A=set(A)
    print(len(A))

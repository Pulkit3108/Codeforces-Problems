q=int(input())
for _ in range(q):
    n=int(input())
    A=list(map(int,input().split()))
    x=sum(A)
    if(x%n==0):
        print(x//n)
    else:
        print(x//n+1)

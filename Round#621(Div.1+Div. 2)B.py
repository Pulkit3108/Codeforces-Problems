t=int(input())
for _ in range(0,t):
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    d=max(A)
    a=0
    if(x in A):
        a=1
    else:
        a=max(2,(x+d-1)//d)
    print(a)


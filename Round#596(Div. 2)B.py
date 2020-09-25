t=int(input())
for _ in range(t):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    c=100000000000
    for i in range(0,n-d+1):
        A=set()
        for j in range(i,i+d):
            A.add(a[j])
        c=min(c,len(A))
    print(c)


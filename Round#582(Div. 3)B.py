t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    c=0
    r=1000000000000000000000000000000000000
    for i in range(n-1,-1,-1):
        if(A[i]>r):
            c+=1
        r=min(r,A[i]);
    print(c)





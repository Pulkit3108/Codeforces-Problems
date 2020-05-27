T=int(input())
for _ in range(0,T):
    n=int(input())
    A=list(map(int,input().split()))
    A.sort()
    ans=1
    for i in range(n-1,-1,-1):
        if(A[i]<=i+1):
            ans+=i+1
            break
    print(ans)

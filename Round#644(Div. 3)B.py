T=int(input())
for _ in range(0,T):
    N=int(input())
    S=list(map(int,input().split()))
    m=10000000000000000
    for i in range(0,N-1):
        for j in range(i+1,N):
            m=min(m,abs(S[i]-S[j]))
    print(m)

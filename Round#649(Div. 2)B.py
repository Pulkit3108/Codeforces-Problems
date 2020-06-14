T=int(input())
for _ in range(0,T):
    n=int(input())
    P=list(map(int,input().split()))
    P1=list()
    for i in range(0,n):
        if(i==0 or i==n-1 or (P[i-1]<P[i])!=(P[i]<P[i+1])):
            P1.append(P[i])
    print(len(P1))
    print(' '.join(map(str,P1)))



   


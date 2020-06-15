n=int(input())
A=list(map(int,input().split()))
k=0
for i in range(0,2*n):
    if(A[0]!=A[i]):
        k=1
        break;
if(k==0):
    print(-1)
else:
    s1=0
    s2=0
    B=list()
    C=list()
    for i in range(0,n):
        s1+=A[i]
        B.append(A[i])
    for j in range(n,2*n):
        s2+=A[j]
        C.append(A[j])
    if(s1==s2):
        r=1
        for i in range(0,n):
            if(r==0):
                break
            for j in range(0,n):
                if(B[i]!=C[j]):
                    t=B[i]
                    B[i]=C[j]
                    C[j]=t
                    r=0
                    break
        A=B+C
    print(' '.join(map(str,A)))

    

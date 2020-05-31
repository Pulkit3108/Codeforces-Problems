n=int(input())
A=list(map(int,input().split()))
B=list(A)
B.sort()
B=B[::-1]
P=list()
M=[0]*n
ans=0
for i in range(0,n):
    ans+=i*B[i]+1
for i in range(0,n):
    for j in range(0,n):
        if(B[i]==A[j] and M[j]==0):
            M[j]=1
            P.append(j+1)
print(ans)
print(' '.join(map(str,P))) 


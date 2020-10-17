n,m=map(int,input().split())
A=[0]*(m+1)
for i in range(n):
    l,r=map(int,input().split())
    for i in range(l,r+1):
        A[i]+=1
k=A.count(0)-1
print(k)
for i in range(1,m+1):
    if(A[i]==0):
        print(i,end=' ')

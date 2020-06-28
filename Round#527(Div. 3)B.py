n=int(input())
A=list(map(int,input().split()))
A.sort()
c=0
for i in range(0,n,2):
    c+=abs(A[i]-A[i+1])
print(c)
    

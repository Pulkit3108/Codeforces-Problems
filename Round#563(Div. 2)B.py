n=int(input())
A=list(map(int,input().split()))
c1=0
c2=0
for i in range(n):
    if(A[i]%2==0):
        c1+=1
    else:
        c2+=1
if(c1>0 and c2>0):
    A.sort()
print(' '.join(map(str,A))) 

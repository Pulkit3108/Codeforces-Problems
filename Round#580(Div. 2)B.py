N=int(input())
A=list(map(int,input().split()))
n=len(list(filter(lambda x:(x<0),A)))  
p=len(list(filter(lambda x:(x>=0),A))) 
c=0
for i in range(0,N):
    if(A[i]==1 or A[i]==-1):
        continue
    elif(A[i]>0):
        c+=A[i]-1
    elif(A[i]<0):
        c+=(-A[i])-1
if(n%2!=0 and A.count(0)==0):
    c+=2
elif(A.count(0)!=0):
    c+=A.count(0)
print(c)

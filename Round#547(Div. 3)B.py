n=int(input())
A=list(map(int,input().split()))
m=0
x=0
s=0
for i in range(0,n):
    if(A[i]==1):
        s+=1
    else:
        break;
while(s!=0):
    A.append(1)
    s-=1
for i in range(0,len(A)):
    if(A[i]==1):
        x+=1
        m=max(m,x)
    else:
        x=0
print(m)


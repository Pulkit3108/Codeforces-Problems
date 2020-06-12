n,m=map(int,input().split())
A=list(map(int,input().split()))
k=max(A)
s=sum(A)
x=0
a=0
A.sort()
for i in range(0,n):
    if(A[i]>x):
        x+=1
        a+=1
    else:
        a+=1
if(k>x):
    a+=k-x
print(s-a)

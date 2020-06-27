n=int(input())
m=int(input())
A=list()
for _ in range(0,n):
    i=int(input())
    A.append(i)
m1=max(A)
m2=min(A)
a2=m+m1
k=m
for i in range(0,n):
    if(k<=0):
        break
    elif(A[i]<m1):
        k-=(m1-A[i])
        A[i]+=(m1-A[i])
    else:
        continue
a1=max(A)
if(k<=0):
    pass
    print(a1,a2)
else:
    q=k//n
    r=k%n
    if(r==0):
        a1+=q
    else:
        a1+=q+1
    print(a1,a2)

        


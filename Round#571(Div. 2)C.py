A=input()
B=input()
a=len(A)
b=len(B)
X=A[:b]
t=0
c=0
for i in range(b):
    if(B[i]!=X[i]):
        t+=1
if(t%2==0):
    c+=1
for i in range(b,a):
    if(A[i]==A[i-b]):
        if(t%2==0):
            c+=1
    else:
        t+=1
        if(t%2==0):
            c+=1
print(c)

n,m=map(int,input().split())
A=list()
Ar=list()
Ap=list()
for i in range(0,n):
    x=input()
    A.append(x)
    Ar.append(x[::-1])
    if(x==x[::-1]):
        Ap.append(x)
B=list()
for i in range(0,n):
    for j in range(i+1,n):
        if(Ar[i]==A[j]):
            B.append(A[j])     
s=""
for x in B:
    s+=x
if(len(Ap)>0):
    s+=Ap[0]   
for x in range(len(B)-1,-1,-1):
    s+=B[x][::-1]
print(len(s))
print(s)

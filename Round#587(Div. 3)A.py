n=int(input())
s=input()
A=list(s)
c=0
for i in range(0,n,2):
    if(A[i]==A[i+1]):
        c+=1
        if(A[i]=='a'):
            A[i]='b'
        elif(A[i]=='b'):
            A[i]='a'
print(c)
for i in A:
    print(i,end='')



n=int(input())
k=int(input())
A=int(input())
B=int(input())
c=0
while(n!=1):
    if(k==1 or k>n):
        c+=(n-1)*A
        break
    elif(n%k!=0):
        c+=(n%k)*A
        n-=n%k
    else:
        c+=min(B,(n-n//k)*A)
        n=n//k
print(c)

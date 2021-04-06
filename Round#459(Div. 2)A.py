n=int(input())
a=[0]*(n+1)
f1=0
f2=1
k=0
while(k<n+1):
    a[k]=1
    f1=f2
    f2=k
    k=f1+f2
s=''
for i in range(1,n+1):
    if(a[i]==0):
        s+='o'
    else:
        s+='O'
print(s)

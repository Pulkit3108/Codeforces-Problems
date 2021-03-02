n=int(input())
a=list(map(int,input().split()))
f=[0]*700
c=0
for i in range(n):
    if(a[i]==0):
        continue
    elif(f[a[i]]==0):
        c+=1
        f[a[i]]=1
print(c)

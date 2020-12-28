n=int(input())
a=list(map(int,input().split()))
b=[0]*1001
c=list()
for i in range(n-1,-1,-1):
    if(b[a[i]]==0):
        b[a[i]]=1
        c.append(a[i])
print(len(c))
print(' '.join(map(str,c[::-1])))

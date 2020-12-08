n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if(a[i]>k):
        break
    else:
        c+=1
for i in range(n-1,-1,-1):
    if(a[i]>k):
        break
    else:
        c+=1
print(min(c,n))

n=int(input())
a=list(map(int,input().split()))
c=a.count(1)
print(c)
for i in range(1,n):
    if(a[i]==1):
        print(a[i-1],end=' ')
print(a[n-1])

n=int(input())
a=list(map(int,input().split()))
s=[0]*1000000
for i in range(0,n):
    for j in range(i+1,n):
        x=a[i]+a[j]
        s[x]+=1
print(max(s))


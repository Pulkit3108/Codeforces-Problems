n,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
f=-1
for i in range(n):
    s+=min(a[i],8)
    if(a[i]>8 and i<n-1):
        a[i+1]+=a[i]-8
    if(s>=k):
        f=i+1
        break
print(f)

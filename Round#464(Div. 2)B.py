n,k=map(int,input().split())
a=list(map(int,input().split()))
t=0
b=0
r=n+1
for i in range(k):
    if(n%a[i]<r):
        r=n%a[i]
        t=i+1
        b=n//a[i]
        if(r==0):
            break
print(t,b)
        

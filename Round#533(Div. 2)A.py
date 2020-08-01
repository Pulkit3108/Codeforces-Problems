n=int(input())
A=list(map(int,input().split()))
m=100000000000000
t=1
for i in range(1,101):
    x=m
    s=0
    for j in range(0,n):
        if(abs(i-A[j])>1):
            s+=abs(i-A[j])-1
        else:
            continue
    m=min(m,s)
    if(m!=x):
        t=i
print(t,m)

        

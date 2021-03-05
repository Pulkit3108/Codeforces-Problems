n,d=map(int,input().split())
x=list(map(int,input().split()))
if(n==1):
    print(0)
else:
    x.sort()
    c=0
    for i in range(n):
        for j in range(i,n):
            if(x[j]-x[i]<=d and j-i+1>c):
                c=j-i+1         
    print(n-c)

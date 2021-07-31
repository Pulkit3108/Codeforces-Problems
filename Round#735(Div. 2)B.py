import sys
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    x=-sys.maxsize
    s=max(0,n-200)
    for i in range(s,n):
        for j in range(i+1,n):
            x=max(x,(i+1)*(j+1)-k*(a[i]|a[j]))
    print(x) 
    

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(1,n):
        if(a[i-1]<=a[i]):
            c=1
            break 
    if(c==0):
        print("NO")
    else:
        print("YES")

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(0,n,2):
        print(-a[i+1],a[i],end=' ')
    print()
        

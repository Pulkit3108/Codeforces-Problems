for _ in range(int(input())):
    n,m=map(int,input().split())
    if(n>m):
        n,m=m,n
    if(n==1 and m>2):
        print(-1)
    else:
        print(2*m-2-(n+m)%2)
    

t=int(input())
for _ in range(t):
    n,m,r,c=map(int,input().split())
    print(max(abs(n-r)+abs(m-c),abs(1-r)+abs(1-c),abs(n-r)+abs(1-c),abs(1-r)+abs(m-c)))

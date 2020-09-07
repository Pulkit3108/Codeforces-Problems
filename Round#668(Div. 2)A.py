t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    p1=p[::-1]
    print(' '.join(map(str,p1)))

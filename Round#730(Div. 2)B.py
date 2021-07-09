for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    r=sum(a)%n
    print(r*(n-r))

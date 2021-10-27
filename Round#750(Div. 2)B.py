for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c1=a.count(1)
    c0=a.count(0)
    print((1<<c0)*c1)


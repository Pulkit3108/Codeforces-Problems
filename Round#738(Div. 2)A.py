for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=a[0]
    for i in range(1,n):
        t=t&a[i]
    print(t)

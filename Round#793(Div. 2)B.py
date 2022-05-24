for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    b=(1<<32)-1
    for i in range(n):
        if(p[i]!=i):
            b&=p[i]
    print(b)

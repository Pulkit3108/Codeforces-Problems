for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if((c+i+1)<a[i]):
            c+=a[i]-(i+1+c)
    print(c)


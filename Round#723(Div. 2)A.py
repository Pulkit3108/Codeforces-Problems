for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=a[:n]
    c=a[-1:-(n+1):-1]
    for i in range(n):
        print(b[i],c[i],end=' ')
    print()

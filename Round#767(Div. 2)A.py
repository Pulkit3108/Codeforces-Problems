for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    r=list()
    for i in range(n):
        r.append([a[i],b[i]])
    r.sort()
    for i in range(n):
        if(k<r[i][0]):
            break
        else:
            k+=r[i][1]
    print(k)


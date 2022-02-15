for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    check=False
    for i in range(n):
        if(p[i]!=i+1):
            check=True
            break
    if(check):
        j=p.index(i+1)
        t=p[i:j+1]
        p=p[:i]+t[::-1]+p[j+1:]
    print(*p)





        

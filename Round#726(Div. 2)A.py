for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    if(sum(a)/n!=1):
        if(sum(a)>n):
            c=sum(a)-n
        else:
            c=1
    print(c)

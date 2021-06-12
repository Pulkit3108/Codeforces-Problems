for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(sum(a)%n!=0):
        print(-1)
    else:
        c=0
        k=sum(a)//n
        for i in a:
            if(k<i):
                c+=1
        print(c)

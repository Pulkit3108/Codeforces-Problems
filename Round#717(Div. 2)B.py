for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        x=0
        for j in range(i+1):
            x=x^a[j]
        f1=0
        t=0
        for j in range(i+1,n):
            t=t^a[j]
            if(t==x):
                f1=1
                t=0
        if(t==0 and f1):
            c=1
            break
    if(c==1):
        print("YES")
    if(c==0):
        print("NO")

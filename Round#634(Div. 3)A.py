T=int(input())
for _ in range(0,T):
    n=int(input())
    x=0
    a=0
    if(n>2):
        x=1
        if(n%2==0):
            a=n//2-1
        else:
            a=n//2
    if(x==1):
        print(a)
    else:
        print(0)
    





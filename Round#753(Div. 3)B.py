for _ in range(int(input())):
    x0,n=map(int,input().split())
    r=n%4
    if(r==0):
        d=0
    if(r==1):
        d=n
    if(r==2):
        d=-1
    if(r==3):
        d=-n-1
    if(x0&1):
        print(x0+d)
    else:
        print(x0-d)

    
    

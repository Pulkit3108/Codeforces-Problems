for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    if((sum(a)+x+y)%2==0):
        print('Alice')
    else:
        print('Bob')

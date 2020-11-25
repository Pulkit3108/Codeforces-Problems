t=int(input())
for _ in range(t):
    n=int(input())
    if(n%2==0):
        for i in range(n,0,-1):
            print(i,end=' ')
    else:
        print(n,end=' ')
        for i in range(1,n):
            print(i,end=' ')
    print()

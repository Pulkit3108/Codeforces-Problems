t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in a:
        if(i%2==0):
            print(i,end=' ')
    for i in a:
        if(i%2!=0):
            print(i,end=' ')
    print()

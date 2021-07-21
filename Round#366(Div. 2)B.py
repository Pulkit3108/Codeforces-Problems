n=int(input())
a=list(map(int,input().split()))
x=2
for i in a:
    if(i%2==0):
        x=3-x
    print(x)

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    k=0
    if(n<=2):
        k=1
    else:
        k=(n-3)//x+2
    print(k)

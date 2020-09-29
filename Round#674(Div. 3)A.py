t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    k=1
    if(n>2):
        if((n-2)%x==0):
            k+=(n-2)//x
        else:
            k+=(n-2)//x+1
    print(k)

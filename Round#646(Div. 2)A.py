T=int(input())
for _ in range(0,T):
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    e=0
    o=0
    c=0
    for i in range(0,n):
        if(A[i]%2==0):
            e+=1
        else:
            o+=1
    a=min(x,o)
    for i in range(1,a+1,2):
        b=x-i
        if(b<=e):
            c=1
    if(c==1):
        print("Yes")
    else:
        print("No")

        


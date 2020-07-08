t=int(input())
for _ in range(0,t):
    n,d=map(int,input().split())
    A=list(map(int,input().split()))
    q=A[0]
    y=d
    for i in range(1,n):
        if(y>=(i*A[i])):
            y-=(i*A[i])
            q+=A[i]
        elif(y>0):
            x=y//i
            y-=(i*x)
            q+=x
        else:
            break
    print(q)


t=int(input())
for _ in range(t):
    n=int(input())
    X=list(map(int,input().split()))
    A=[0]*110
    for i in X:
        A[i]+=1
    if(A[0]==0):
        print(0)
    elif(A[0]==1):
        for i in range(1,101):
            if(A[i]==0):
                break
        print(i)
    else:
        for k in range(1,101):
            if(A[k]==0):
                break
        for i in range(0,101):
            if(A[i]<2):
                break
        print(k+i)


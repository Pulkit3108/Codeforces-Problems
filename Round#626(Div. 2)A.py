t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    index=0
    for i in range(0,n):
        if(A[i]%2==0):
            index=i+1
            c=1
            break
    if(len(A)==1 and A[0]%2!=0):
        print(-1)
    elif(index!=0):
        print(1)
        print(index)
    else:
        print(2)
        print(1,2)
    
    



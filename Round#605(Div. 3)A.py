T=int(input())
for _ in range(0,T):
    A=list(map(int,input().split()))
    A.sort()
    x=0
    if(A[0]==A[1] and A[1]==A[2]):
        x=0
    elif(A[0]!=A[1] and A[1]==A[2]):
        if(A[0]+1==A[1]):
            A[0]+=1
        else:
            A[0]+=1
            A[1]-=1
            A[2]-=1
    elif(A[0]==A[1] and A[1]!=A[2]):
        if(A[1]+1==A[2]):
            A[2]-=1
        else:
            A[2]-=1
            A[1]+=1
            A[0]+=1
    elif(A[0]!=A[1] and A[1]!=A[2]):
        A[0]+=1
        A[2]-=1
    x=abs(A[0]-A[1])+abs(A[0]-A[2])+abs(A[1]-A[2])
    print(x)

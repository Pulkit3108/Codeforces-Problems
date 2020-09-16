def lot(A):
    if(len(A)==0):
        return(1)
    elif(len(A)==1):
        B=list()
        return(lot(B)+1)
    else:
        A.sort()
        B=list()
        k=A[0]
        for i in range(1,len(A)):
            if(A[i]%k!=0):
                B.append(A[i])
        return(lot(B)+1)
n=int(input())
A=list(map(int,input().split()))
print(lot(A)-1)

T=int(input())
for _ in range(0,T):
    N=int(input())
    A=list(map(int,input().split()))
    C=list(A)
    C.sort()
    c1=0
    c0=0
    B=list(map(int,input().split()))
    for i in range(0,N):
        if(B[i]==0):
            c0+=1
        else:
            c1+=1
    if(c1!=0 and c0!=0):
        A.sort()        
    if(C==A):    
        print("Yes")
    else:
        print("No")

    


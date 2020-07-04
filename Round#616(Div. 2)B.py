t=int(input())
for _ in range(0,t):
    n=int(input())
    A=list(map(int,input().split()))
    c=1
    p=-1
    s=n
    for i in range(0,n):
        if(A[i]<i):
            break
        p=i
    for i in range(n-1,-1,-1):
        if(A[i]<(n-1)-i):
            break
        s=i
    if(s<=p):
        print("Yes")
    else:
        print("No")
 


    


    
    



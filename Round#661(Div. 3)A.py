t=int(input())
for _ in range(0,t):
    n=int(input())
    A=list(map(int,input().split()))
    A.sort()
    c=1
    for i in range(0,n-1):
        if(abs(A[i]-A[i+1])<=1):
            continue
        else:
            c=0
            break
    if(c==1):
        print("YES")
    else:
        print("NO")

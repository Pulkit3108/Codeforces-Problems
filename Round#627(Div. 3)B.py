t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    c=0
    for i in range(0,n-2):
        for j in range(i+2,n):
            if(A[i]==A[j]):
                c=1
                break
    if(c==0):
        print("NO")
    else:
        print("YES")




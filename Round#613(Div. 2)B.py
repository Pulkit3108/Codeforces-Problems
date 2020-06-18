t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    c=1
    s1=0
    s2=0
    for i in range(0,n):
        s1+=A[i]
        s2+=A[n-i-1]
        if(s1<=0 or s2<=0):
            c=0
            break
    if(c):
        print("YES")
    else:
        print("NO")

        

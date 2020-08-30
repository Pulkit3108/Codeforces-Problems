q=int(input())
for _ in range(q):
    n=int(input())
    A=list(map(int,input().split()))
    p=A.index(1)
    c1=1
    c2=1
    for i in range(1,n):
        if(A[(p-i+n)%n]!=i+1):
            c1=0
        if(A[(p+i+n)%n]!=i+1):
            c2=0
    if(c1==1 or c2==1):
        print("YES")
    else:
        print("NO")

t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(b[i]==b[j]):
                c=1
                break
    if(c==1):
        print("YES")
    else:
        print("NO")

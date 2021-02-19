t=int(input())
for _ in range(t):
    n=int(input())
    h=list(map(int,input().split()))
    k=1
    c=0
    for i in range(n):
        c+=(h[i]-i)
        if(c<0):
            k=0
            break
    if(k==1):
        print('YES')
    else:
        print('NO')
   
        

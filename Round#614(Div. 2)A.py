t=int(input())
for _ in range(0,t):
    n,s,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=10000000
    for i in range(0,k+1):
        if(s-i not in a and s-i>0):
            m=min(m,abs(i))
        elif(s-i<1):
            break
    for i in range(0,k+1):
        if(s+i not in a and s+i<n+1): 
            m=min(m,abs(i))
        elif(s+i>n):
            break
    print(m)

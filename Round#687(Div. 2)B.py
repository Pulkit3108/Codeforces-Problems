t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    m=1000000000
    for i in range(1,101):
        cnt=0
        j=0
        while(j<n):
            if(c[j]!=i):
                cnt+=1
                j+=k
            else:
                j+=1
        m=min(cnt,m)
    print(m)

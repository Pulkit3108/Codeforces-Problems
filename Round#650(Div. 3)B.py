t=int(input())
for _ in range(0,t):
    n=int(input())
    A=list(map(int,input().split()))
    e=0
    o=0
    m=0
    for i in A:
        if(i%2==0):
            e+=1
        else:
            o+=1
    if((n%2==0 and e!=o) or (n%2!=0 and (e)!=(o+1))):
        print(-1)
    else:
        for i in range(0,n):
            if((A[i]%2)!=(i%2)):
                m+=1
        print(m//2)


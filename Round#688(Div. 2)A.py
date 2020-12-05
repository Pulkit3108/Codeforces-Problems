t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    tr=[0]*102
    for i in a:
        tr[i]+=1
    c=0
    for i in b:
        if(tr[i]==1):
            c+=1
    print(c)

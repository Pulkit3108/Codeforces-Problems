
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(0,n):
        if(a[i]==1):
            c1+=1
        else:
            c2+=1
    if((c1%2==0 and c1!=0) or (c1==0 and c2%2==0)):
        print('YES')
    else:
        print('NO')

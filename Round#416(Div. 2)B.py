n,m=map(int,input().split())
p=[0]+list(map(int,input().split()))
for _ in range(m):
    l,r,x=map(int,input().split())
    c=0
    for i in range(l,r+1):
        if(p[i]<p[x]):
            c+=1
    if(l+c==x):
        print('Yes')
    else:
        print('No')
 

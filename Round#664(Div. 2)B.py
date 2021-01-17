n,m,sx,sy=map(int,input().split())
print(sx,sy)
s=[0]*(m+1)
s[sy]=1
for i in range(1,n+1):
    if(i!=sx):
        print(i,sy)
d=0
for j in range(1,m+1):
    if(s[j]!=1):
        if(d==0):
            for i in range(n,0,-1):
                print(i,j)
            s[j]=1
            d=1
        elif(d==1):
            for i in range(1,n+1):
                print(i,j)
            s[j]=1
            d=0
        

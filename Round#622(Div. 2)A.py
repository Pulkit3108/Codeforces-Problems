t=int(input())
for _ in range(0,t):
    A=[(0,0,1),(1,0,0),(0,1,0),(1,1,1),(1,1,0),(1,0,1),(0,1,1)]
    A=list(map(int,input().split()))
    A.sort(reverse=True)
    a=A[0]
    b=A[1]
    c=A[2]
    ans=0
    if(a>0):
        a-=1
        ans+=1 
    if(b>0):
        b-=1 
        ans+=1
    if(c>0):
        c-=1 
        ans+=1
    if(a>0 and b>0):
        a-=1 
        b-=1 
        ans+=1
    if(a>0 and c>0):
        a-=1
        c-=1 
        ans+=1
    if(b>0 and c>0):
        b-=1
        c-=1
        ans+=1 
    if(a>0 and b>0 and c>0):
        ans+=1
    print(ans)



    
    



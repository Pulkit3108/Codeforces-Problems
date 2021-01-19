t=int(input())
for i in range(t):
    l,r,m=map(int,input().split())
    d=r-l
    for i in range(l,r+1):
        m1=m%i
        m2=i-(m%i)
        if(i<=m and m1<=d):
            a=i
            b=r
            c=r-m1
            break
        elif(m2<=d):
            a=i
            b=r-m2
            c=r
            break
    print(a,b,c)
        
    
        

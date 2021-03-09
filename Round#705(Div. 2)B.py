def check(a,b,h,m):
    r=[0,1,5,-1,-1,2,-1,-1,8,-1]
    if(r[a//10]==-1 or r[a%10]==-1 or r[b//10]==-1 or r[b%10]==-1):    
        return(False)
    a1=r[b%10]*10+r[b//10]
    b1=r[a%10]*10+r[a//10]
    if(a1<h and b1<m):
        return(True)
    else:
        return(False)
t=int(input())
for i in range(t):
    h,m=map(int,input().split())
    hh,mm=input().split(':')
    h1=int(hh)
    m1=int(mm)
    while(h1!=0 or m1!=0):
        if(check(h1,m1,h,m)):
            break
        if(m1==m-1):
            h1=(h1+1)%h
        m1=(m1+1)%m
    print('{0}{1}:{2}{3}'.format(h1//10,h1%10,m1//10,m1%10))
    

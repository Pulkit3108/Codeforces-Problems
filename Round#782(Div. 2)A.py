for _ in range(int(input())):
    n,r,b=map(int,input().split())
    m=r%(b+1)
    t=''
    for i in range((r//(b+1))):
        t+='R'
    s=''
    for i in range(b+1):
        if(i>0):
            s+='B'
        s+=t
        if(m>0):
            s+='R'
            m-=1
    print(s)
    

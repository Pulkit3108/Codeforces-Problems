for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if(a+b>n-2 or abs(a-b)>1):
        print(-1)
    else:
        p=list(range(1,n+1))
        if(a==b):
            i=1
            while(a!=0):
                p[i],p[i+1]=p[i+1],p[i]
                a-=1
                i+=2
        elif(a>b):
            p.reverse()
            i=0
            while(a!=0):
                p[i],p[i+1]=p[i+1],p[i]
                a-=1
                i+=2
        else:
            i=0
            while(b!=0):
                p[i],p[i+1]=p[i+1],p[i]
                b-=1
                i+=2
        print(' '.join(map(str,p)))
        
        
        

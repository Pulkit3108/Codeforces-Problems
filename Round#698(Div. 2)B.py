t=int(input())
for _ in range(t):
    q,d=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        s=1
        if(d*10>i):
            x=d
            s=i-x
            while(s>0 and s%10!=0):
                x+=d
                s=i-x
        if(s>=0):
            print('YES')
        else:
            print('NO')
        
        
                
            
        

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    flag=True
    o=0
    for i in range(n-1,0,-1):
        while(a[i-1]>=a[i] and a[i-1]>0):
            o+=1
            a[i-1]//=2
        if(a[i-1]==a[i]):
            flag=False
            break
    if(flag):
        print(o)
    else:
        print(-1)
        

        
    
    

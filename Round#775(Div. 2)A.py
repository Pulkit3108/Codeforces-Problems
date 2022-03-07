for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=0
    r=0
    c=0
    for i in range(n):
        if(a[i]==0):
            c+=1
            break
        else:
            l=i
    for i in range(n-1,-1,-1):
        if(a[i]==0):  
            break
        else:
            r=i
    if(c==0):
        print(0)
    else:
        print(r-l)
    
    
    



        

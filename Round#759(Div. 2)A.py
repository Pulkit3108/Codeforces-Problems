for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    h=1+a[0]
    for i in range(1,n):
        if(a[i-1]==1 and a[i]==1):
            h+=5
        elif(a[i-1]==0 and a[i]==0):
            h=-1
            break
        else:
            h+=a[i]
    print(h)
    
        
        
        

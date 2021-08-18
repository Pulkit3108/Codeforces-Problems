for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list()
    if(a[n-1]==0):
        for i in range(0,n+1):
            print(i+1,end=' ')
        print()
    elif(a[0]==1):
        print(n+1,end=' ')
        for i in range(0,n):
            print(i+1,end=' ')
        print()
    else:
        c=-1
        for i in range(0,n-1):
            if(a[i]==0 and a[i+1]==1):
                c=i
                break
        for i in range(0,n):
            print(i+1,end=' ')
            if(i==c):
                print(n+1,end=' ')
        print()
        
        
    
    

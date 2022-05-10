for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    i=j=0
    while(i<n):
        if(a[i]<0):
            a[j]*=-1
            a[i]*=-1
            j+=1
        i+=1
    if(a==sorted(a)):
        print('YES')
    else:
        print('NO')
        
    
    

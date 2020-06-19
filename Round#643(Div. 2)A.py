t= int(input())
for _ in range(0,t):
    a,k=map(int,input().split())
    a=str(a)
    x=a
    for i in range(0,k-1):
        if(min(x)=='0'):
            break
        else:
            q=int(x)+(int(max(x))*int(min(x)))
            x=str(q)       
    print(x)
    

    

t=int(input())
for _ in range(0,t):
    n=int(input())
    c=0
    if(n==1):
        c=0
    else:
        while(n!=1):
            if(n%6==0):
                c+=1
                n=n//6
            elif(n%3==0):
                c+=1
                n=n*2
            else:
                c=-1
                break
    print(c)
    
    

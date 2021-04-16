n,k=map(int,input().split())
if(k==1):
    print(n)
else:
    c=0
    while(n!=0):
        n=n//2
        c+=1
    print(pow(2,c)-1)
 
        
                
    

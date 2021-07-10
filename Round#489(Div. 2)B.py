def gcd(a,b):
    if(b==0):
        return(a)
    return(gcd(b,a%b))
l,r,x,y=map(int,input().split())
if(y%x!=0):
    print(0)
else:
    c=0
    k=y//x
    i=1
    while(i*i<=k):
        if(k%i==0):
            j=k//i
            if((l<=j*x and j*x<=r) and (l<=i*x and i*x<=r) and gcd(i,j)==1):
                if(i*i==k):
                    c+=1
                else:
                    c+=2
        i+=1
    print(c)        
        
    

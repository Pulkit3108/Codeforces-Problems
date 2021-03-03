def sd(n): 
    if(n%2==0): 
        return(2)
    i=3
    while(i*i<=n): 
        if(n%i==0): 
            return i; 
        i+=2; 
    return n; 
p,y=map(int,input().split())
k=-1
for i in range(y,p,-1):
    a=sd(i)
    if(a>p):
        k=i
        break
print(k)

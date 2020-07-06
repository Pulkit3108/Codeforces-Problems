def countSetBits(n): 
    if(n==0): 
        return(0)
    else:  
        return((n&1)+countSetBits(n>>1)) 
t=int(input())
for _ in range(0,t):
    a=int(input())
    x=countSetBits(a)
    print(pow(2,x))

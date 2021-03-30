def gcd(a,b):
    if(b==0):
        return(a)
    else:
        return(gcd(b,a%b))
t=int(input())
for _ in range(t):
    n=int(input())
    k=1
    for i in range(n,n+10000): 
        c=i
        s=0
        while(c!=0):
            s+=c%10
            c=c//10
        k=gcd(i,s)
        if(k!=1):
            break
    print(i)  

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
for _ in range(int(input())):
    n=int(input())
    a=2
    while(1):
        if(gcd(a,n-a-1)==1):
            break
        a+=1
    print(a,n-a-1,1)
    

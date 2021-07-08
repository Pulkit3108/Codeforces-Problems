def gcd(a,b):
    if(b==0):
        return(a)
    return(gcd(b,a%b))
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a==b):
        print(0,0)
    elif(abs(a-b)==1):
        print(1,0)
    else:
        k=abs(a-b)
        s=(a//k+1)*k
        print(k,min(a%k,s-a))

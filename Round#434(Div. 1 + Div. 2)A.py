def getGCD(a,b):
    if(a==0):
        return b
    return getGCD(b%a,a)
n,k=map(int,input().split())
print((n*10**k)//getGCD(10**k,n))

                     
                     

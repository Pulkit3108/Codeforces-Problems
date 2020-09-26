def gcd(a,b):
    if(b==0):
        return(a)
    else:
        return(gcd(b,a%b))
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if(gcd(a,b)!=1):
        print("Infinite")
    else:
        print("Finite")
  

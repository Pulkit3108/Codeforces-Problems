'''def prime(n) : 
    if(n<=1): 
        return False
    if(n<=3): 
        return True
    if(n%2==0 or n%3==0): 
        return False
    i=5
    while(i*i<=n) : 
        if(n%i== 0 or n%(i+2)==0) : 
            return False
        i=i+6
    return True'''
t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    if(n==1):
        c=0
    elif(n==2):
        c=1
    elif(n==3 or n%2==0):
        c=2
    else:
        c=3
    print(c)

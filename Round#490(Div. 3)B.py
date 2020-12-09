import math
def div(n):
    A=list() 
    i=1
    while(i<=math.sqrt(n)): 
        if(n%i==0):     
            if(n/i==i):  
                A.append(i) 
            else: 
                A.append(i)
                A.append(n//i)
        i=i+1
    return(sorted(A))
n=int(input())
s=input()
Q=div(n)
x=s
for i in Q:
    q=x[:i]
    x=q[::-1]+x[i:n] 
print(x)

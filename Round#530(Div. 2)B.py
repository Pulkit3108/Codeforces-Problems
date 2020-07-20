import math  
n=int(input())
a=int(math.sqrt(n))
if(n==1):
    print(2)
elif(((a)*(a))>=n):
    print(a+a)
elif(((a)*(a+1))>=n):
    print(a+a+1)
elif(((a+1)*(a+1))>=n):
    print(a+a+2)




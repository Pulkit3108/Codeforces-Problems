n=int(input())
d=int(input())
e=int(input())
c=n
i=0
while(i*d<=n): 
    c=min(c,(n-i*d)%(5*e))
    i+=1
print(c)
    


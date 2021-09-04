a,b=map(int,input().split())
k=1
for i in range(a+1,b+1):
   k=(k*i%10)&10
print(k) 

n=int(input())
c=0
for i in range(n-1,0,-1):
    if(i%(n-i)==0):
        c+=1 
print(c)

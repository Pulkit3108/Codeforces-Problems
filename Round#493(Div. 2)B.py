n,b=map(int,input().split())
a=list(map(int,input().split()))
x=list()
i=0
e=0
o=0
while(i<n):
    if(e==o and o!=0):
        e=0
        o=0
        x.append(abs(a[i]-a[i-1]))
    if(a[i]%2==0):
        e+=1
    elif(a[i]%2!=0):
        o+=1
    i+=1
c=0
x.sort()
for i in x:
    b-=i
    if(b<0):
        break
    else:
        c+=1
print(c)    
    

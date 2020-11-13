n,d=map(int,input().split())
x=list(map(int,input().split()))
s=set()
c=2
for i in range(0,n-1):
    if(x[i+1]-x[i]>2*d):
        c+=2
    elif(x[i+1]-x[i]==2*d):
        c+=1
print(c)

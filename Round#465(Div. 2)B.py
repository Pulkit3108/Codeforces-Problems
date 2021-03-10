n=int(input())
s=input()
x,y=0,0
c=0
g=-1
z=0
for i in s:
    # print(x,y,p,c,z)
    if(i=='U'):
        y+=1
        if(z==1 and g!=-1):
            c+=1
        g=-1
    if(i=='R'):
        x+=1
        if(z==2 and g!=-1):
            c+=1
        g=-1
    if(x>y):
        z=1
    if(y>x):
        z=2
    if(x==y and x!=0):
        if(z==1):
            g=0
        elif(z==2):
            g=1
print(c)
    
    















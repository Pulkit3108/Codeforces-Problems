x,y,z=map(int,input().split())
g,p,b=map(int,input().split())
c=1
if(g<x):
    c=0
else:
    g=g-x
    if((g+p)<y):
        c=0
    else:
        w=g+p-y+b
        if(w<z):
            c=0
        else:
            c=1

if(c==1):
    print("YES")
else:
    print("NO")





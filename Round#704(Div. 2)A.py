t=int(input())
for _ in range(t):
    p,a,b,c=map(int,input().split())
    x1,x2,x3=0,0,0
    if(p<a):
        x1=a-p
    else:
        c1=0
        c1=p//a
        if(p%a!=0):
            c1+=1
        x1=a*c1-p
    if(p<b):
        x2=b-p
    else:
        c1=0
        c1=p//b
        if(p%b!=0):
            c1+=1
        x2=b*c1-p
    if(p<c):
        x3=c-p
    else:
        c1=0
        c1=p//c
        if(p%c!=0):
            c1+=1
        x3=c*c1-p
    print(min(x1,x2,x3))
    

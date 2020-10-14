import sys
n,h,a,b,k=map(int,input().split())
for i in range(k):
    ta,fa,tb,fb=map(int,input().split())
    if(ta-tb==0):
        print(abs(fa-fb))
    else:
        if(fa>=a and fa<=b):
            t=abs(ta-tb)+abs(fa-fa)+abs(fb-fa)
        elif(fb>=a and fb<=b):
            t=abs(ta-tb)+abs(fa-fb)+abs(fb-fb)
        else:
            t1=abs(ta-tb)+abs(fa-a)+abs(fb-a)
            t2=abs(ta-tb)+abs(fa-b)+abs(fb-b)
            t=min(t1,t2)
        print(t)

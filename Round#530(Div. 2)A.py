w,h=map(int,input().split())
u1,d1=map(int,input().split())
u2,d2=map(int,input().split())
a=w
while(h!=0):
    a+=h
    if(h==d1):
        a-=u1
    elif(h==d2):
        a-=u2
    h-=1
    if(a<0):
        a=0
print(a)




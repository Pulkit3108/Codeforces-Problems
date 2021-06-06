V1,V2,V3,VM=map(int,input().split())
a=[0]*3
a[0]=max(2*VM+2,V1)
a[1]=max(2*VM+1,V2)
a[2]=max(VM,V3)
if(2*V1<a[0] or 2*V2<a[1] or 2*V3<a[2] or 2*VM<a[2]):
    print(-1)
else:
    for i in a:
        print(i)



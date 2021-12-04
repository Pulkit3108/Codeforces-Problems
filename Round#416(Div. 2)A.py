a,b=map(int,input().split())
flag=False
i=1
while(1):
    if(i&1):
        a-=i
    else:
        b-=i
    i+=1
    if(a<0):
        flag=True
    if(a<0 or b<0):
        break
if(flag):
    print('Vladik')
else:
    print('Valera')

n,k=map(int,input().split())
a=list(map(int,input().split()))
f=n
t=2*n
l=0
for i in range(k):
    while(a[i]>=4):
        a[i]-=4
        if(f>0):
            f-=1
        elif(t>=2):
            t-=2
        else:
            print('NO')
            exit()
for i in range(k):
    if(a[i]==3):
        a[i]=0
        if(f>0):
            f-=1
        elif(t>=2):
            t-=2
        else:
            print('NO')
            exit()
for i in range(k):
    if(a[i]==2):
        a[i]=0
        if(t>0):
            t-=1
        elif(f>0):
            f-=1
            l+=1
        elif(l>=2):
            l-=2
        else:
            print('NO')
            exit()
l+=2*f+t
if(sum(a)>l):
    print('NO')
else:
    print('YES')
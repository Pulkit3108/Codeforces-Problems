t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    c=0
    f1=[0]*(m+2)
    b1=[0]*(m+2)
    f2=[0]*(m+2)
    b2=[0]*(m+2)
    for i in range(n):
        if(f1[a[i]]==0):
            f1[a[i]]=1
        else:
            break
    t1=i
    for i in range(t1,n):
        if(b1[a[i]]==0):
            b1[a[i]]=1
        else:
            break
    for i in range(n-1,-1,-1):
        if(b2[a[i]]==0):
            b2[a[i]]=1
        else:
            break
    t2=i
    for i in range(t2,-1,-1):
        if(f2[a[i]]==0):
            f2[a[i]]=1
        else:
            break
    k1=0
    k2=0
    k3=0
    k4=0
    l1=0
    l2=0
    for i in range(1,m+1):
        if(f1[i]==1):
            l1+=1
        if(b1[i]==1):
            l1+=1
        if(f2[i]==1):
            l2+=1
        if(b2[i]==1):
            l2+=1
        if(f1[i]==0 and f1[i+1]==1):
            k1=1
        if(b1[i]==0 and b1[i+1]==1):
            k2=1
        if(f2[i]==0 and f2[i+1]==1):
            k3=1
        if(b2[i]==0 and b2[i+1]==1):
            k4=1
    if(k1==0 and k2==0 and k3==0 and k4==0 and l1==n and l2==n and t1!=t2+1):
        print(2)
        print(t1,n-t1)
        print(t2+1,n-t2-1)
    elif(k1==0 and k2==0 and l1==n):
        print(1)
        print(t1,n-t1)
    elif(k3==0 and k4==0 and l2==n):
        print(1)
        print(t2+1,n-t2-1)
    else:
        print(0)
        

        


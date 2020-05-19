k=int(input())
if(k<25):
    print(-1)
    exit()
n=m=0
for i in range(5,k+1):
    if(k%i==0 and k//i>=5):
        n=i
        m=k//i
        break
if(n==0):
    print(-1)
else:
    s=['a','e','i','o','u']
    x=k=0
    for i in range(0,n):
        x=k
        for j in range(0,m):
            print(s[x],end='')
            x+=1
            if(x==5):
                x=0
        k+=1
        if(k==5):
            k=0

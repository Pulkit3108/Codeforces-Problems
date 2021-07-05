import math
for _ in range(int(input())):
    n,a,b=list(map(int,input().split()))
    c=0
    if(a==1):
        if((n-1)%b==0):
            c=1
    else:
        t=n-1
        i=0
        while(t>=0):
            if(t%b==0):
                c=1
                break
            i+=1
            t=n-pow(a,i)
    if(c==1):
        print('Yes')
    else:
        print('No')

t=int(input())
for _ in range(t):
    x=int(input())
    n=0
    s=1
    a=0
    i=1
    while(n<x):
        n+=(s*(s+1))//2
        a+=1
        s+=int(pow(2,i))
        i+=1
    if(n>x):
        a-=1
    print(a)
        
        
        

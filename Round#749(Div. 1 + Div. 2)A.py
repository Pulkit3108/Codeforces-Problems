def notprime(n):
    for i in range(2,n//2+1):
        if(int(n%i)==0):
            return True
    return False
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    if(s&1==0 or notprime(s)):
        print(n)
        print(' '.join(map(str,range(1,n+1))))
    else:
        o=-1
        for i in range(n):
            if(a[i]&1):
                s-=a[i]
                o=i;
                break 
        t=[i for i in range(1,n+1) if(i-1)!=o]
        print(len(t))
        print(' '.join(map(str,t)))
    

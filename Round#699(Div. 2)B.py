t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    m=max(h)
    c=0
    a=0
    for i in h:
        c+=m-i
    if(k>c):
        a=-1
    else:
        for i in range(k):
            f=0
            for j in range(n-1):
                if(h[j]<h[j+1]):
                    a=j+1
                    h[j]+=1
                    f=1
                    break
        if(f==0):
            a=-1
    print(a)
        
    
    
        

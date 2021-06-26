for _ in range(int(input())):
    n=int(input())
    a=list(range(1,n+1))
    if(n%2!=0):
        a[-2],a[-1]=a[-1],a[-2]
        n-=1
    for i in range(0,n,2):
        a[i],a[i+1]=a[i+1],a[i]        
    print(' '.join(map(str,a)))

        



t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    e=set()
    for i in range(n):
        if(a[i]%2==0):
            e.add(a[i])
    x=len(e)
    c=0
    e=set(sorted(e))
    while(x!=0):
        q=e.pop()
        q=q//2
        c+=1
        if(q%2==0):
            e.add(q)
        x=len(e)    
    print(c)
        

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=dict()
    for i in a:
        f=m.setdefault(i,0)
        f+=1
        m[i]=f
    for k in range(1,n+1):
        print(max(k,len(m)),end=' ')
    print()
        
    



        

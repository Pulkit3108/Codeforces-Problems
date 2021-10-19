for _ in range(int(input())):
    n,m=map(int,input().split())
    k=set()
    for _ in range(m):
        a,b,c=map(int,input().split())
        k.add(b)
    m=-1
    for i in range(1,n+1):
        if(i not in k):
            m=i
            break
    for i in range(1,n+1):
        if(i==m):
            continue
        else:
            print(m,i) 
            
    

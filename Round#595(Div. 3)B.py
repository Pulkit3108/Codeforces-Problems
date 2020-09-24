t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    for i in range(0,n):
        x=p[i]
        c=1
        while(x-1!=i):
            c+=1
            x=p[x-1]
        print(c,end=' ')
    print()
    

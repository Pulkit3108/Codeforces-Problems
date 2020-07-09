t=int(input())
for _ in range(0,t):
    n,k=map(int,input().split())
    x=n-(k-1)
    if(x>0 and x%2==1):
        print("YES")
        for i in range(0,k-1):
            print(1,end=' ')
        print(x)
        continue
    y=n-2*(k-1)
    if(y>0 and y%2==0):
        print("YES")
        for i in range(0,k-1):
            print(2,end=' ')
        print(y)
        continue
    print("NO")

    

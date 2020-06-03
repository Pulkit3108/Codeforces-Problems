T=int(input())
for _ in range(0,T):
    n=int(input())
    if(n%4!=0):
        print("NO")
    else:
        print("YES")
        for i in range(1,n//2+1):
            print(2*i,end=' ')
        for i in range(1,n//2):
            print(2*i-1,end=' ')
        print(3*n//2 - 1)
        


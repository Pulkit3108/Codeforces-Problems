for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    z=a.count(0)
    if(z):
        print(n-z)
    elif(len(a)==len(set(a))):
        print(n+1)
    else:
        print(n)
    
    

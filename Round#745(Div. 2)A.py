mod=1e9+7
for _ in range(int(input())):
    n=int(input())
    f=1
    for i in range(3,2*n+1):
        f=int((f*i)%mod)
    print(f)
    
    

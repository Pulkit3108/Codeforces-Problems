mod=998244353
for _ in range(int(input())):
    n=int(input())
    if(n&1):
        print(0)
        continue
    p=1
    for i in range(1,n//2+1):
        p=(p*i)%mod
    p=(p*p)%mod
    print(p)

    

m=int(1e9+7)
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=1;
    for i in range(k):
        s=(s*n)%m;
    print(s)

        
    

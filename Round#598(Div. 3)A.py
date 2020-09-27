t=int(input())
for _ in range(t):
    a,b,n,S=map(int,input().split())
    k=S//n
    k=min(a,k)
    a-=k
    S-=n*k
    S-=min(b,S)
    if(S==0):
        print("YES")
    else:
        print("NO")

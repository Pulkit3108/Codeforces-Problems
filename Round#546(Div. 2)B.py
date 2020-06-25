n,k=map(int,input().split())
ans=n+(n+1)+min(n-k,k-1)+n-1
print(ans)

n,m,r=map(int,input().split())
s=list(map(int,input().split()))
b=list(map(int,input().split()))
x=min(s)
sh=r//x
a=r%x
a+=max(b)*sh
print(max(a,r))

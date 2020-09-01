n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    c+=i&1
print(min(c,n-c))

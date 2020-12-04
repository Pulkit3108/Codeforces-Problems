n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n):
    if(i+1>a[i]):
        b[i]=i+1
    else:
        q=(a[i]-(i+1)+n)//n
        b[i]=i+1 + q*n
print(b.index(min(b))+1)

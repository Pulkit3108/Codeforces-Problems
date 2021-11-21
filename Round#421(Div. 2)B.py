n,a=map(int,input().split())
b=(n*a //180)
b=max(1,min(n-2,b))
k=b
for i in range(max(1,b-2),min(n-2,b+2)+1):
    if(abs(180*i-n*a)<abs(180*k-n*a)):
        k=i;
print(2,1,k+2)

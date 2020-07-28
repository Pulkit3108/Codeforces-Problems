n,v=map(int,input().split())
x=min(n-1,v)
if(x<n-1):
    x=v-1;
    for i in range(1,n-v+1):
        x+=i;
print(x)


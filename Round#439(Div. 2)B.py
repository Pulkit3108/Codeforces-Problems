a,b=map(int,input().split())
if(b-a>=10):
    print(0)
else:
    k=1
    for i in range(a+1,b+1):
        k*=i%10
        k%=10
    print(k) 

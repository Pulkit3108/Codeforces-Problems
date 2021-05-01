n=int(input())
a=0
b=0
for _ in range(n):
    x,y=map(int,input().split())
    if(x>=0):
        a+=1
    else:
        b+=1
if(a>1 and b>1):
    print('No')
else:
    print('Yes')    

T=int(input())
for _ in range(T):
    count=0
    a,b=map(int,input().split())
    x=b-a
    if(x>0):
        if(x%2==0):
            count=2
        else:
            count=1
    elif(x<0):
        if(x%2==0):
            count=1
        else:
            count=2
    print(count)
            

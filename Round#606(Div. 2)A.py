t=int(input())
for _ in range(t):
    n=int(input())
    a=0
    b=0
    for i in range(1,10):
        b=b*10+1
        for j in range(1,10):
            if(b*j<=n):
                a+=1
    print(a)
        


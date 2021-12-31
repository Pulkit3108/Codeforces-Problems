a,b=map(int,input().split())
c,d=map(int,input().split())
for i in range(1000):
    for j in range(1000):
        if(b+a*i==d+c*j):
            print(b+a*i)
            exit(0)
print(-1)

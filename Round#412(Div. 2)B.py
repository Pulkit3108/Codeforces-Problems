def do(n,p):
    t=(n//50)%475
    for i in range(25):
        t=(t*96+42)%475
        if(26+t==p):
            return True
    return False
p,x,y=map(int,input().split())
for i in range(500):
    for j in range(500):
        if(x+100*i-50*j>=y and do(x+100*i-50*j,p)):
            print(i)
            exit()



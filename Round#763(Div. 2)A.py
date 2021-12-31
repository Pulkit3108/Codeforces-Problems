def robot(n,i,f): 
    if(f>=i):
        return f-i 
    else: 
        return 2*(n-i)+i-f 
for _ in range(int(input())): 
    n,m,rb,cb,rd,cd=map(int,input().split()) 
    print(min(robot(n,rb,rd),robot(m,cb,cd))) 

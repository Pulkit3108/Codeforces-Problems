for _ in range(int(input())):
    a,b,c,x,y=map(int,input().split())
    if(max(x-a,0)+max(y-b,0)>c):
        print('NO')
    else:
        print('YES')
        
    
    

for _ in range(int(input())):
    n=int(input())
    c=0
    while(n>0):
        if(n%11==0 or n%111==0):
            c=1
            break
        else:
            n-=111
    if(c==0):
        print('NO')
    else:
        print('YES')
        

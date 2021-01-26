t=int(input())
for _ in range(t): 
    n=int(input())
    c=1
    if(n%2!=0 or (n//2>1 and (n//2)%2!=0)):
        print('YES')
    else:
        print('NO')

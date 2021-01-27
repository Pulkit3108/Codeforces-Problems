t=int(input())
for _ in range(t): 
    n=int(input())
    c=0
    if(n%2020==0 or n%2021==0 or n%4041==0 or (n%4041)%2020==0 or (n%4041)%2021==0):
        print('YES')
    else:
        print('NO')
    

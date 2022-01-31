for _ in range(int(input())):
    n=int(input())
    s=input()
    if(n==1 or (n==2 and s[0]!=s[1])):
        print('YES')
    else:
        print('NO')

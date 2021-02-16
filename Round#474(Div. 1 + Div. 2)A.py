s=input()
k=1
if(sorted(s)!=list(s)):
    print('NO')
else:
    a=s.count('a')
    b=s.count('b')
    c=s.count('c')
    if((a!=0 and b!=0 and c!=0) and (c==a or c==b)):
        print('YES')
    else:
        print('NO')

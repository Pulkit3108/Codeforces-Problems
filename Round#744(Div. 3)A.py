for _ in range(int(input())):
    s=input()
    ca=0
    cb=0
    cc=0
    for i in s:
        if(i=='A'):
            ca+=1
        if(i=='B'):
            cb+=1
        if(i=='C'):
            cc+=1
    if(ca+cc==cb):
        print('YES')
    else:
        print('NO')

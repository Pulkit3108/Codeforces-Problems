for _ in range(int(input())):
    s=input()
    c=input()
    flag=False
    for i in range(len(s)):
        if(i&1):
            continue
        elif(s[i]==c):
            flag=True
    if(flag):
        print('YES')
    else:
        print('NO')
    
    



        

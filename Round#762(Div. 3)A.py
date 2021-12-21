for _ in range(int(input())):
    s=input()
    if(len(s)&1):
        print('NO')
    else:
        flag=True
        for i in range(0,len(s)//2):
            if(s[i]!=s[i+len(s)//2]):
                flag=False
                break
        if(flag):
            print('YES')
        else:
            print('NO')
        
    

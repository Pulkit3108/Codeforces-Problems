for _ in range(int(input())):
    s=input()+'*'
    t=input()+'*'
    a=list()
    b=list()
    j=0
    for i in range(len(s)):
        if(s[j]!=s[i]):
            a.append(s[j:i])
            j=i
    j=0
    for i in range(len(t)):
        if(t[j]!=t[i]):
            b.append(t[j:i])
            j=i
    if(len(a)!=len(b)):
        print('NO')
    else:
        flag=True
        for i in range(len(a)):
            if(a[i][0]!=b[i][0] or len(a[i])>len(b[i])):
                flag=False
                break
        if(flag):
            print('YES')
        else:
            print('NO')
        
        
    

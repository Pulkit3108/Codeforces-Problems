for _ in range(int(input())):
    n=int(input())
    s=input()
    o=0
    c=0
    ch=s[0]
    for i in range(n):
        if(c==0):
            c+=1
            ch=s[i]
            continue
        if(s[i]==ch):
            c+=1
        else:
            if(c&1):
                o+=1
                c=0
            else:
                c=1
                ch=s[i]
    print(o)
        
        
        
    
    

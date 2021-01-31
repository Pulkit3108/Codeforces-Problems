t=1
for _ in range(t):
    n=int(input())
    s=input()
    s1=list(s)
    s2=list(s)
    f=list()
    b=list()
    q=0
    for i in range(len(s1)-1):
        if(s1[i]=='B'):
            s1[i]=='W'
            f.append(i+1)
            if(s1[i+1]=='B'):
                s1[i+1]='W'
            elif(s1[i+1]=='W'):
                s1[i+1]='B'
    if(s1[-1]=='B'):
        for i in range(len(s2)-1):
            if(s2[i]=='W'):
                s2[i]=='B'
                b.append(i+1)
                if(s2[i+1]=='B'):
                    s2[i+1]='W'
                elif(s2[i+1]=='W'):
                    s2[i+1]='B'
        if(s2[-1]=='B'):
            q=-1
    else:
        q=1
    if(q==0):
        print(-1)
    elif(q==1):
        print(len(f))
        print(' '.join(map(str,f)))
    elif(q==-1):
        print(len(b))
        print(' '.join(map(str,b)))
        
                
            
        

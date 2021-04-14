t=int(input())
for _ in range(t):
    n=int(input())
    s=list()
    t=list()
    for i in range(n):
        a=list(input())
        s.append(a)
    for i in range(n):
        for j in range(n):
            if(s[i][j]=='*'):
                t.append(i)
                t.append(j)
    if(t[0]==t[2]):
        if(t[0]==n-1):
            s[t[0]-1][t[1]]='*'
            s[t[2]-1][t[3]]='*'
        else:
            s[t[0]+1][t[1]]='*'
            s[t[2]+1][t[3]]='*'
    elif(t[1]==t[3]):
        if(t[1]==n-1):
            s[t[0]][t[1]-1]='*'
            s[t[2]][t[3]-1]='*'
        else:
            s[t[0]][t[1]+1]='*'
            s[t[2]][t[3]+1]='*'
    else:
        s[t[0]][t[3]]='*'
        s[t[2]][t[1]]='*'
    for i in range(n):
        print(''.join(map(str,s[i])))
    
                
    

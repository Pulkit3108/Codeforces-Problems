t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    t=list()
    m=list()
    c=1
    for i in range(len(s)):
        if(s[i]=='T'):
            t.append(i)
        else:
            m.append(i)
    if(len(t)!=2*len(m)):
        c=0
    else:
        for i in range(len(m)):
            if(m[i]<t[i] or m[i]>t[i+len(m)]):
                c=0
                break
    if(c==0):
        print('NO')
    else:
        print('YES')

        

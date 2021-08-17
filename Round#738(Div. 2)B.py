for _ in range(int(input())):
    n=int(input())
    s=input()
    a=list(s)
    b=list(s)
    i=0
    while(s[i]!='R' and s[i]!='B'):
        if(i%2==0):
            a[i]='B'
            b[i]='R'
        else:
            a[i]='R'
            b[i]='B'
        i+=1
        if(i>=n):
            break
    cb=0
    ca=0
    for i in range(1,n):
        if(a[i-1]==a[i]):
            ca+=1
        if(b[i-1]==b[i]):
            cb+=1
    if(ca>cb):
        s=list(b)
    else:
        s=list(a)
    for i in range(n):
        if(s[i]=='?'):
            if(i>0):
                if(s[i-1]=='R'):
                    s[i]='B'
                elif(s[i-1]=='B'):
                    s[i]='R'
            elif(i<n-1):
                if(s[i+1]=='R'):
                    s[i]='B'
                elif(s[i-1]=='B'):
                    s[i]='R'
    print(''.join(map(str,s)))

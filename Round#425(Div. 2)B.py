g=input()
p=input()
for _ in range(int(input())):
    flag=True
    s=input()
    t=p
    if('*' in t):
        if(len(t)<=len(s)):
            t=t.replace('*','*'*(abs(len(t)-len(s))+1))
        elif(len(t)==len(s)+1):
            t=t.replace('*','')
    if(len(s)!=len(t)):
        flag=False
    else:
        for i in range(len(s)):
            if(t[i]=='*'):
                if(s[i] in g):
                    flag=False
                    break
            elif(t[i]=='?'):
                if(s[i] not in g):
                    flag=False
                    break
            else:
                if(t[i]!=s[i]):
                    flag=False
                    break
        else:
            flag=True
    if(flag):
        print("YES")
    else:
        print("NO")

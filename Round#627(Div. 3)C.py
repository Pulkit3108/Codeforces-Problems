t=int(input())
for _ in range(t):
    s=input()
    l=0
    r=1
    B=list()
    B.append(0)
    for i in range(0,len(s)):
        if(s[i]=='L'):
            l+=1
        else:
            r+=1
            B.append(i+1)
    B.append(len(s)+1)
    c=0
    for i in range(0,len(B)-1):
        c=max(c,B[i+1]-B[i])
    print(c)
    



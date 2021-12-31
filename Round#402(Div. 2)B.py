n,k=map(int,input().split())
s=str(n)[::-1]
c=0
d=0
if(s.count('0')<k):
    print(len(s)-1)
else:
    for i in range(len(s)):
        if(s[i]=='0'):
            c+=1
        else:
            d+=1
        if(c==k):
            break
    print(d)


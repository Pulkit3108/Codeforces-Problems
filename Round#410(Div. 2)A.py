s=input()
c=0
for i in range(0,len(s)//2):
    if(s[i]!=s[len(s)-i-1]):
        c+=1
if(c==1 or (c==0 and len(s)&1)):
    print('YES')
else:
    print('NO')


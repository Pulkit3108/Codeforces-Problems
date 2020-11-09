s=input()
a1='aouie'
a2='aouien'
c=1
n=len(s)
i=0
while(i<n):
    if(s[i] in a2):
        i+=1
        continue
    elif(i+1!=n):
        if(s[i+1] not in a1):
            c=0
            break
        else:
            i+=2
    else:
        i+=2
if(s[n-1] not in a2):
    c=0
if(c==1):
    print('YES')
else:
    print('NO')

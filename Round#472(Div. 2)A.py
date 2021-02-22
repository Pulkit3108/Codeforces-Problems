n=int(input())
s=input()
a=['MM','YY','CC']
c=1
for i in a:
    if(i in s):
        c=0
        break
if(c==0):
    print('No')
elif(s[0]=='?' or s[n-1]=='?'):
    print('Yes')
else:
    if('??' in s or 'Y?Y' in s or 'M?M' in s or 'C?C' in s):
        print('Yes')
    else:
        print('No')

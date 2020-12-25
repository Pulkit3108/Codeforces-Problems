n=int(input())
s=input()
c=1
if(('11' in s) or ('000' in s) or (n==1 and s=='0') or (s[0]=='0' and s[1]=='0') or (s[n-2]=='0' and s[n-1]=='0')):
    c=0
if(c==1):
    print('Yes')
else:
    print('No')

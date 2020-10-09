n=int(input())
s=input()
a=[0]*26
for i in s:
    a[ord(i)-97]+=1
c=0

for i in a:
    if(i>1):
        c=1
        break
if(c==0 and n!=1):
    print('No')
else:
    print('Yes')

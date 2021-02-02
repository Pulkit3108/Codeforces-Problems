s=input()
l=0
p=0
for i in s:
    if(i=='-'):
        l+=1
    elif(i=='o'):
        p+=1
if(l==0 or p==0 or l%p==0):
    print('YES')
else:
    print('NO')

n=int(input())
a=input()
b=input()
a00=0
a11=0
a01=0
a10=0
for i in range(n):
    if(a[i]=='0' and b[i]=='0'):
        a00+=1
    elif(a[i]=='1' and b[i]=='1'):
        a11+=1
    elif(a[i]=='0' and b[i]=='1'):
        a01+=1
    elif(a[i]=='1' and b[i]=='0'):
        a10+=1
print(a00*a11+a01*a10+a10*a00)

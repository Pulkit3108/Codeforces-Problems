s=input()
a=0
b=0
m=0
for i in s:
    print(a,b,m)
    if(i=='a'):
        a+=1
        m=max(b+1,m+1)
    else:
        b=max(a+1,b+1)
print(max(a,max(b,m)))

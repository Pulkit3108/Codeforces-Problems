n=int(input())
s=input()
c=0
m=0
t=""
for i in s:
    if(i.isupper()):
        c=0
        t=""
    elif(i in t):
        continue
    else:
        c+=1
        t+=i
    m=max(m,c)
print(m)


f,l=input().split()
s=f[0]
for i in range(1,len(f)):
    if(ord(f[i])>=ord(l[0])):
        break
    s+=f[i]
s+=l[0]
print(s)

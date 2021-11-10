k1=input()
k2=input()
s=input()
t=""
for i in s:
    if i.isalpha():
        j=k1.index(i.lower())
        if i.isupper():
            t+=k2[j].upper()
        else:
            t+=k2[j]
    else:
        t+=i
print(t)

    

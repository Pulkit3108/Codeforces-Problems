n=int(input())
s=input()
s+='p'
c=0
a=0
for i in s:
    if(i=='x'):
        c+=1
    else:
        if(c>2):
            a+=c-2
        c=0
print(a)
    

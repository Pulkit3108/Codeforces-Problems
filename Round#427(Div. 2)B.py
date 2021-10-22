k=int(input())
n=input()
d=list()
for i in n:
    d.append(ord(i)-ord('0'))
d.sort()
s=sum(d)
c=0
for i in d:
    if(s<k):
        s+=9-i
        c+=1
print(c)

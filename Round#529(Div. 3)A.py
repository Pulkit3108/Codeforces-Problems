n=int(input())
s=input()
A=list()
j=1
i=0
while(i<len(s)):
    A.append(s[i])
    j+=1
    i+=j
print(''.join(map(str,A)))
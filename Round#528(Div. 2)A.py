s=input()
n=len(s)
x=0
if(n%2==0):
    x=n//2-1
else:
    x=n//2
s1=""
i=x
j=x+1
while(i>=0 or j<n):
    if(i>=0):
        s1+=s[i]
    if(j<n):
        s1+=s[j]
    i-=1
    j+=1
print(s1)

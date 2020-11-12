s=list(input())
t=list(input())
c=0
while(1):
    i=len(s)-1-c
    j=len(t)-1-c
    if(i>=0 and j>=0 and s[i]==t[j]):
        c+=1
    else:
        break
print(len(s)+len(t)-2*c)
        

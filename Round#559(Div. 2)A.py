n=int(input())
s=input()
s=list(s)
c1=0
c2=0
for i in range(n-1,-1,-1):
    if(s[i]=='+'):
        c1+=1
    else:
        c1-=1
    c2=max(c1,c2)
print(c2)

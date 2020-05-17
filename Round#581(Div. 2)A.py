s=input()
ans=0
l=len(s)
if(s==0):
    print(0)
    exit()
if(len(s)%2==0):
    ans=l//2
else:
    if '1' in s[1:len(s)]:
        ans=(l+1)//2
    else:
        ans=l//2
print(ans)

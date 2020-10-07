n,k=map(int,input().split())
s=input()
r='a'
for i in range(n//2-1,-1,-1):
    if(s[:i+1]==s[i+1:]):
        r=i
        break
if(r=='a'):
    print(s*k)
else:
    print(s[:r+1]+s[:r+1]*k)

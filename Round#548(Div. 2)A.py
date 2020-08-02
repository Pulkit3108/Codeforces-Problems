n=int(input())
s=input()
x=0
for i in range(0,len(s)):
    if(int(s[i])%2==0):
        x+=i+1
print(x)




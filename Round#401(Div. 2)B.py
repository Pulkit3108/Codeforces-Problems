n=int(input())
s=sorted(input())
m=sorted(input())
j=0
for i in range(n):
    if(m[i]>s[j]):
        j=j+1
mx=j
j=n-1
for i in range(n-1,-1,-1):
    if(m[j]>=s[i]):
        j=j-1
mn=j+1
print(mn)
print(mx)

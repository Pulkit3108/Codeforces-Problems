s=input()
n=int(input())
f1=False
f2=False
for _ in range(n):
    t=input()
    if(s[0]==t[0] and s[1]==t[1]):
        f1=True
        f2=True
    if(s[0]==t[1]):
        f1=True
    if(s[1]==t[0]):
        f2=True
if(f1 and f2):
    print('YES')
else:
    print('NO')

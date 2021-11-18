n,m=map(int,input().split())
s=input()
t=input()
a=list(range(1,n+1))
for i in range(m-n+1):
    b=[]
    c=0
    for j in range(n):
        if s[j]!=t[i+j]:
            b.append(j+1)
            c=c+1
    if(c<len(a)):
        a=b
print(len(a))
print(' '.join(map(str,a)))

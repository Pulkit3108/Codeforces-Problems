n=int(input())
A=['']*n
for i in range(0,n):
    s=input()
    A[i]=s[0]
a=[0]*26
for k in A:
    a[ord(k)-ord('a')]+=1
x=0
for m in a:
    x1=x2=0
    x1=m//2
    x2=m-x1
    if(x1==0 or x1==1):
        x1=0
    else:
        x1=(x1*(x1-1))//2
    if(x2==0 or x2==1):
        x2=0
    else:
        x2=(x2*(x2-1))//2
    x+=x1+x2
print(x)

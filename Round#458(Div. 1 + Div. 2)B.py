n=int(input())
a=list(map(int,input().split()))
f=[0]*(max(a)+1)
for i in a:
    f[i]+=1
c=0
for i in f:
    if(i%2!=0):
        c=1
        break
if(c==0):
    print('Agasa')
else:
    print('Conan')

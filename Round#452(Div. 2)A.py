n=int(input())
a=list(map(int,input().split()))
c1=0
c2=0
for i in a:
    if(i==1):
        c1+=1
    if(i==2):
        c2+=1
r=c1
if(c1>c2):
    r=c2+int((c1-c2)/3)
print(r)

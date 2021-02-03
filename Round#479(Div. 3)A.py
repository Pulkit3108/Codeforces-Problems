n,k=map(int,input().split())
a=list(map(int,str(n)))
j=len(a)-1
for i in range(k):
    if(a[j]==0):
        j-=1
    else:
        a[j]-=1       
s=''
q=0
while(j!=-1):
    s+=str(a[q])
    q+=1
    j-=1
print(int(s))

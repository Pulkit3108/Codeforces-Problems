n=int(input())
A=list(map(int,input().split()))
c=0
e1=0
o1=0
e2=0
o2=0
for j in range(0,n):
    if(j%2==0):
        o1+=A[j]
    else:
        e1+=A[j]
for i in range(0,n):
    if(i%2==0):
        o1-=A[i]
    else:
        e1-=A[i]
    if(e2+o1==o2+e1):
        c+=1
    if(i%2==0):
        o2+=A[i]
    else:
        e2+=A[i]
print(c)
        

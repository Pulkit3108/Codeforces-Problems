N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a1=a2=0
b1=b2=0
for i in A:
    if(i%2==0):
        a1+=1
    elif(i%2!=0):
        a2+=1
for j in B:
    if(j%2==0):
        b1+=1
    elif(j%2!=0):
        b2+=1
s=min(a1,b2)+min(a2,b1)
print(s)

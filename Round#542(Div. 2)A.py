N=int(input())
A=list(map(int,input().split()))
p=0
n=0
for x in A:
    if(x>0):
        p+=1
    elif(x<0):
        n+=1
if(p>=(N+1)//2):
    print(1)
elif(n>=(N+1)//2):
    print(-1)
else:
    print(0)

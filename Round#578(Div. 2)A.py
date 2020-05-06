R=[0]*10
def Left():
    for i in range(0,10):
        if R[i]==0:
            R[i]=1
            break
 
def Right():
    i=9
    while(i>=0):
        if R[i]==0:
            R[i]=1
            break
        i-=1
n=int(input())
s=input()
for x in s:
    if x=='L':
        Left()
    elif x=='R':
        Right()
    else :
        R[int(x)]=0
for m in R:
    print(m,end='')

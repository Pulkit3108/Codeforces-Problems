def sot(x):
    c=0
    while(x>0):
        c+=x%10
        x//=10
    return(c)
a=int(input())
while(sot(a)%4!=0):
    a+=1
print(a)

def dig(x):
    s=0
    while(x!=0):
        s+=x%10
        x=x//10
    return(s)
k=int(input())
i=0
while(k!=0):
    i+=1
    if(dig(i)==10):
        k-=1
print(i)

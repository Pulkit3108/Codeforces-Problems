n=int(input())
a=list(map(int,input().split()))
k=sum(a)
av=k/n
c=0
if(av<4.5):
    a.sort()
    s=int(n*4.5)-k
    if(n%2!=0):
        s+=1
    q=0
    for i in range(n):
        if(q>=s):
            break
        else:
            q+=5-a[i]
            c+=1
print(c)

n=int(input())
s=input()
m=0
a=''
for i in range(1,n):
    k=s[i-1:i+1]
    w=0
    for j in range(1,n):
        k1=s[j-1:j+1]
        if(k==k1):
            w+=1
    if(w>m):
        a=k
        m=w
print(a)
    

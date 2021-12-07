n,k=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
m=0
while(s/n+0.5<k):
    s+=k
    n+=1
    m+=1
print(m)


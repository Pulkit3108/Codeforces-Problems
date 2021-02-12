k,n,s,p=map(int,input().split())
a=n//s
if(n%s!=0):
    a+=1
q=k*a
m=q//p
if(q%p!=0):
    m+=1
print(m)
    


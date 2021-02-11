n,A,B=map(int,input().split())
s=list(map(int,input().split()))
S=sum(s)
q=sorted(s[1:],reverse=True)
q=s[:1]+q
k=int((s[0]*A)//B)
c=0
for i in range(1,n):
    if(S<=k):
        break
    else:
        S-=q[i]
        c+=1
print(c)

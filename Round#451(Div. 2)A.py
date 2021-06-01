n=int(input())
r=n%10
if(r>5):
    n+=(10-r)
else:
    n-=r
print(n)

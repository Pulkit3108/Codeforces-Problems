n,S=map(int,input().split())
c=0
if(S%n==0):
    c=S//n
else:
    c=S//n + 1
print(c)

n,A,B,C,T=map(int,input().split())
t=list(map(int,input().split()))
if(B>C):
    print(n*A)
else:
    c=0
    t.sort()
    for i in t:
        c+=(T-i)*(C-B)+A 
    print(c)

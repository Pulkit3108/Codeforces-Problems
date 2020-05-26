import sys
T=int(input())
for _ in range(0,T):
    n,a,b,c,d=map(int,input().split())
    x=0
    if(abs(c-d)<=(n*abs(a+b)) and (c+d)>=(n*(a-b))):
        x=1
    if(x==1):
        print("YES")
    else:
        print("NO")





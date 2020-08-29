n=int(input())
A=list(map(int,input().split()))
s=sum(A)
m=max(A)
b=s-m
if(s%2==0 and m<=b):
    print("YES")
else:
    print("NO")


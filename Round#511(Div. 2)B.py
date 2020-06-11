n=int(input())
c=0
for i in range(n):
    x,y=map(int,input().split())
    c=max(c,x+y)
print(c)

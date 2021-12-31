R,D=map(int,input().split())
c=0
for _ in range(int(input())):
    x,y,r=map(int,input().split())
    d=(x*x+y*y)**(0.5)
    if(r+d<=R and d-r>=R-D):
        c+=1
print(c)

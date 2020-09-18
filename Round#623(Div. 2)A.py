n=int(input())
for _ in range(n):
    a,b,x,y=map(int,input().split())
    a1=b*x
    a2=b*(a-x-1)
    a3=y*a
    a4=(b-y-1)*a
    print(max(a1,a2,a3,a4))

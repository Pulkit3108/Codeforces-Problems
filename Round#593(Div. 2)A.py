t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    c1=c//2
    c=0
    k=min(c1,b)
    c+=k*3
    b-=k
    b1=b//2
    k=min(b1,a)
    c+=k*3
    print(c)


t=int(input())
for _ in range(t):
    a0,a1,a2=map(int,input().split())
    b0,b1,b2=map(int,input().split())
    s=0
    m=min(a0,b2)
    a0-=m
    b2-=m
    m=min(b0,a1)
    b0-=m
    a1-=m
    m=min(a2,b1)
    a2-=m
    b1-=m
    s+=2*m
    s-=2*min(a1,b2)
    print(s)

   

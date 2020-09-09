t=int(input())
for _ in  range(t):
    n=int(input())
    A=list(map(int,input().split()))
    z=A.count(0)
    o=A.count(1)
    if(z>=o):
        print(z)
        print(' '.join(map(str,[0]*z)))
    else:
        if(o%2!=0):
            o-=1
        print(o)
        print(' '.join(map(str,[1]*o)))

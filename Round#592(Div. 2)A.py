t=int(input())
for _ in range(t):
    a,b,c,d,k=map(int,input().split())
    c1=a//c
    if(a%c!=0):
        c1+=1
    c2=b//d
    if(b%d!=0):
        c2+=1
    if(c1+c2>k):
        print(-1)
    else:
        print(k-c2,c2)

t=int(input())
for _ in range(0,t):
    L,v,l,r=map(int,input().split())
    if(l%v!=0):
        c1=l//v
    else:
        c1=l//v-1
    c2=L//v
    x=r//v
    c2-=x
    print(c1+c2)

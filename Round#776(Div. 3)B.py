def fvlad(x,a):
    f=(x//a)+(x%a)
    return f
for _ in range(int(input())):
    l,r,a=map(int,input().split())
    v=fvlad(r,a)
    m=((r//a)*a)-1;
    if(m>=l):
        v=max(v,fvlad(m,a));
    print(v)
    



        

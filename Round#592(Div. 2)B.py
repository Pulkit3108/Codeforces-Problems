t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=0
    c1=0
    c2=0
    p=s[::-1]
    if(s.count('1')==0):
        c=n
    else:
        c1=s.index('1')
        c2=p.index('1')
        a=min(c1,c2)
        a=n-a
        c=2*a
    print(c)


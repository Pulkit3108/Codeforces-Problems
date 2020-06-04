T=int(input())
for _ in range(0,T):
    s=input()
    A=list(s)
    c1=0
    c2=0
    z=0
    o=0
    c=0
    for i in range(0,len(A)):
        if(A[i]=='0'):
            z+=1
        else:
            o+=1
    c=min(z,o)
    for i in range(0,len(A)):
        if(A[i]=='0'):
            z-=1
            c1+=1
        else:
            o-=1
            c2+=1
        c=min(c,c2+z);
        c=min(c,c1+o);
    print(c)


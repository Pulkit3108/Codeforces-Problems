for _ in range(int(input())):
    n=int(input())
    s=input()
    t=sorted(s)
    l=list()
    for i in range(n):
        if(s[i]!=t[i]):
            l.append(i+1)
    if(len(l)==0):
        print(0)
    else:
        print(1)
        print(len(l),end=' ')
        print(' '.join(map(str,l)))

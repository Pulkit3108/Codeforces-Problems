t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*101
    s=list()
    for i in a:
        b[i]+=1
        if(b[i]>1):
            s.append(i)
    print(' '.join(map(str,sorted(set(a)))),end=' ')
    print(' '.join(map(str,sorted(s))))

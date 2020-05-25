T=int(input())
for _ in range(0,T):
    N=int(input())
    A=list(map(int,input().split()))
    E=list()
    O=list()
    ans=0
    for x in A:
        if(x%2==0):
            E.append(x)
        else:
            O.append(x)
    e=len(E)
    o=len(O)
    if(e%2==0 and o%2==0):
        ans=1
    else:
        for i in range(0,e):
            for j in range(0,o):
                if(abs(E[i]-O[j])==1):
                    ans=1
                    break
    if(ans==1):
        print("YES")
    else:
        print("NO")


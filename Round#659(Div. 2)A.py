t=int(input())  
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))  
    m=max(a)
    S=['a'*(m+1)]*(n+1)
    for i,x in enumerate(a):
        w=''
        if(S[i][x]=='b'):
            w='a'
        else:
            w='b'
        S[i+1]=S[i][:x]+w+S[i][x+1:]
    print('\n'.join(S))


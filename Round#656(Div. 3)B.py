t=int(input())
for _ in range(0,t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list()
    for i in A:
        if(i not in B):
            B.append(i)
    print(' '.join(map(str,B)))


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    k=0
    for i in range(n-1,-1,-1):
        if(s[i]==')'):
            k+=1
        else:
            break
    q=n-k
    if(q<k):
        print('Yes')
    else:
        print('No')

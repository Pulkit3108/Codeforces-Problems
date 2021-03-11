t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    if(n<2*k+1):
        print('NO')
    else:
        c=1
        for i in range(k):
            if(s[i]==s[n-i-1]):
                continue
            else:
                c=0
                break
        if(c==1):
            print('YES')
        else:
            print('NO')

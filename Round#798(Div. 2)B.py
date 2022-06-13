for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    if(n==1):
        print(-1)
    else:
        s=sorted(p)
        for i in range(n):
            if(s[i]==p[i]):
                if(i+1!=n):
                    s[i],s[i+1]=s[i+1],s[i]
                else:
                    s[i],s[i-1]=s[i-1],s[i]
        print(*s)

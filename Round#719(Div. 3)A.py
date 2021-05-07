for _ in range(int(input())):
    n=int(input())
    s=input()
    a=[0]*26
    c=1
    for i in range(1,n):
        if(s[i-1]!=s[i]):
            if(a[ord(s[i-1])-65]==1 or a[ord(s[i])-65]==1):
                c=0
                break
            else:
                a[ord(s[i-1])-65]=1
    if(c==1):
        print('YES')
    else:
        print('NO')

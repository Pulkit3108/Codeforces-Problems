t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    t=list(input())
    c=0
    k=list()
    for i in range(n):
        if(s[i]!=t[i]):
            c+=1
            k.append(i)
            if(c>2):
                break
    if(c==2):
        p=s[k[0]]
        s[k[0]]=t[k[1]]
        t[k[1]]=p
        if(s==t):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

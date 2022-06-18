for _ in range(int(input())):
    n=int(input())
    s=input()
    s='*'+s
    c=0
    for i in range(n,0,-1):
        if(s[i]!=s[i-1]):
            c+=i
        else:
            c+=1
    print(c)

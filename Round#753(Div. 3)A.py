for _ in range(int(input())):
    k=input()
    s=input()
    t=0
    for i in range(len(s)-1):
        t+=abs(k.index(s[i])-k.index(s[i+1]))
    print(t)
    
    

for _ in range(int(input())):
    s=list(input())
    a=min(s)
    s.remove(a)
    b=''.join(map(str,s))
    print(a,b)

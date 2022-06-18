for _ in range(int(input())):
    a,b=map(int,input().split())
    s=list()
    for i in range(min(a,b)):
        s.append('01')
    for i in range(abs(a-b)):
        if(a>b):
            s.append('0')
        else:
            s.append('1')
    print(''.join(map(str,s)))

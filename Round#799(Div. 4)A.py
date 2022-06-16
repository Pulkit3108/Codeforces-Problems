def check(a,b):
    if(a>b):
        return 1
    return 0
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    print(check(b,a)+check(c,a)+check(d,a));    

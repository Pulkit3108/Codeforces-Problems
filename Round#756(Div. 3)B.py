for _ in range(int(input())):
    a,b=map(int,input().split())
    print(min(min(a,b),(a+b)//4))
